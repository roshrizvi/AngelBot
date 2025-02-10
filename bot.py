import discord 
from discord import app_commands
from discord.ext import commands
from datetime import datetime
import asyncio
import test2
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID_YO = int(os.getenv("CHANNEL_ID_YO", 0))
CHANNEL_ID_ANGEL = int(os.getenv("CHANNEL_ID_ANGEL", 0))
GUILD_ID = int(os.getenv("GUILD_ID", 0))

# Set up bot intents
intents = discord.Intents.default()
intents.message_content = True  # Required for commands to work
intents.guilds = True
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

# Setup logging
def setup_logging():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(script_dir, 'bot_logs.log')
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler()
        ]
    )

setup_logging()

@client.event
async def on_ready():
    logging.info(f'{client.user.name} is now active')

    # Register and sync slash commands
    client.tree.clear_commands(guild=discord.Object(id=GUILD_ID))
    client.tree.add_command(hello_command, guild=discord.Object(id=GUILD_ID))
    client.tree.add_command(say, guild=discord.Object(id=GUILD_ID))
    client.tree.add_command(commands_list, guild=discord.Object(id=GUILD_ID))

    try:
        await client.wait_until_ready()
        synced = await client.tree.sync(guild=discord.Object(id=GUILD_ID))
        logging.info(f'Successfully synced {len(synced)} slash command(s)')
    except Exception as e:
        logging.error(f'Failed to sync slash commands: {e}')

    channel = client.get_channel(CHANNEL_ID_YO)
    if channel:
        await channel.send('Bot is online!')

    client.loop.create_task(send_message_task())

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

def is_angel():
    current_time = datetime.now()
    continuous_number = current_time.hour * 100 + current_time.minute
    angels = [111, 222, 333, 444, 555, 1111, 1311, 1422, 1533, 1644, 1755, 2311]
    return continuous_number in angels

async def send_message_task():
    while True:
        if is_angel():
            channel = client.get_channel(CHANNEL_ID_ANGEL)
            if channel:
                await channel.send('ANGEL :pray: local')
                test2.meow()
            await asyncio.sleep(60)
        else:
            await asyncio.sleep(10)

@client.command()
async def hello(ctx):
    await ctx.send("Hello, gang!")

@client.command()
async def add(ctx, *numbers):
    try:
        result = sum(map(int, numbers))
        await ctx.send(f"Result: {result}")
    except ValueError:
        await ctx.send("Please provide valid numbers.")

@client.command()
async def timenow(ctx):
    now = datetime.now()
    await ctx.send(f"Current time: {now.hour}:{now.minute}")

@client.command()
async def send(ctx, channel_id: int, *, message: str):
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send(message)
        await ctx.send(f"Message sent to {channel.mention}")
    else:
        await ctx.send("Invalid channel ID.")

@client.tree.command(name="hello")
async def hello_command(interaction: discord.Interaction):
    """Replies with a hello message."""
    await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!")

@client.tree.command(name="say")
@app_commands.describe(thing_to_say="What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    """Repeats what the user says."""
    await interaction.response.send_message(f"{interaction.user.name} said: '{thing_to_say}'")

@client.tree.command(name="commands")
async def commands_list(interaction: discord.Interaction):
    """Lists all available commands."""
    commands = (
        "**Available Commands:**\n"
        "`!hello` - Greets the user.\n"
        "`!add <num1> <num2> ...` - Adds numbers.\n"
        "`!timenow` - Shows the current time.\n"
        "`!send <channel_id> <message>` - Sends a message to a channel.\n"
        "`/hello` - Slash command to greet.\n"
        "`/say <text>` - Slash command to repeat text.\n"
        "`/commands` - Lists all available commands.\n"
    )
    await interaction.response.send_message(commands, ephemeral=True)

@client.command()
async def dm(ctx, user_id: int, *, message: str):
    user = client.get_user(user_id)
    if user:
        try:
            await user.send(message)
            await ctx.send(f"Message sent to {user.name} successfully!")
        except Exception as e:
            logging.error(f"Error sending DM: {e}")
            await ctx.send("An error occurred while sending the message.")
    else:
        await ctx.send("Invalid user ID.")

client.run(TOKEN)

