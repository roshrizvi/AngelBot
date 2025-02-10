# Discord Bot

A simple Discord bot built using `discord.py` that includes message logging, scheduled messages, and various commands.

## Features
- Logs bot messages and DMs
- Sends scheduled messages based on angel numbers
- Basic bot commands (`!hello`, `!add`, `!timenow`, etc.)
- Slash command support
- Secure token management using `.env`

## Setup

### Prerequisites
- Python 3.10+
- `discord.py` installed

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/yourbot.git
   cd yourbot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your bot token and channel IDs:
   ```sh
   DISCORD_BOT_TOKEN=your_bot_token_here
   CHANNEL_ID_YO=888170772793786459
   CHANNEL_ID_ANGEL=1124822502154174584
   ```
4. Run the bot:
   ```sh
   python bot.py
   ```

## Usage
Use the following commands:
- `!hello` - Greets you
- `!add <num1> <num2> ...` - Adds numbers
- `!timenow` - Shows the current time
- `!send <channel_id> <message>` - Sends a message to a channel
- `!dm <user_id> <message>` - Sends a DM

## Contributing
Feel free to fork and submit pull requests!

## License
MIT License

