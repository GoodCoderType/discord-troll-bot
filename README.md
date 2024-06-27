
# Discord Bot Troll Tool

This project is a Discord bot designed to provide an interactive and entertaining experience within a specified Discord channel. The bot listens for messages in the channel and responds with user-defined replies, packaged in a visually appealing embedded message format.

## Features

- **Interactive Responses**: The bot listens for messages and prompts the user for a reply, which is then sent as an embedded message in the channel.
- **Customizable**: Configure the bot with your token and channel ID via a `config.json` file.
- **Visual Enhancements**: Uses `colorama` for colorful console output and embeds for rich message formatting in Discord.
- 
## Setup 
Go To Discord APi
Create Discord Bot
Add In Server And Enable Intents
Take Bot Token

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/discord-bot-troll-tool.git
   cd discord-bot-troll-tool
   ```

2. **Install the required dependencies**:
   ```bash
   pip install discord.py colorama
   ```

3. **In `config.json` file** with your bot token and channel ID:
   ```json
   {
       "token": "YOUR_BOT_TOKEN",
       "channel_id": "YOUR_CHANNEL_ID"
   }
   ```

## Usage

1. **Run the bot**:
   ```bash
   python bot.py
   ```

2. **Interact with the bot**: The bot will wait for messages in the specified channel. When a message is received, it will prompt you to enter a reply, which it will then send as an embedded message in the channel.

## Contributing

Feel free to submit issues and pull requests for new features or improvements.

## License

This project is licensed under the MIT License.

---
