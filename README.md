

# R2D2 Bot
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/discord.py)
![GitHub License](https://img.shields.io/github/license/luismede/rd2d)
![GitHub Created At](https://img.shields.io/github/created-at/luismede/r2d2-bot)

R2D2 Bot is a simple and customizable Discord bot built using `discord.py`, designed to provide various utility commands, moderation tools, and entertainment features. This bot was inspired by Star Wars' R2-D2, but it serves general purposes on any server.

## Features
- **Customizable Command Prefix**: Set your preferred command prefix in the configuration.
- **Moderation Tools**: Commands for kicking and clearing chat.
- **Ping Command**: Checks the bot's latency.
- **Star Wars API Integration**: Fetches information about Star Wars characters from the SWAPI (Star Wars API).
- **Help Command**: Displays the available commands and how to use them.

## Requirements

- Python 3.8+
- `discord.py` library
- Internet connection (for API requests)

### Installing Dependencies

Before running the bot, make sure to install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Configuration

Create a file named `config.json` in the `config` folder with the following structure:

```json
{
  "prefix": "your-bot-prefix",
  "token": "your-bot-token"
}
```

- **prefix**: The command prefix you'll use to call bot commands (e.g., "!" or "?").
- **token**: Your bot's secret token from Discord's developer portal.

## How to Run

Once you've installed the dependencies and configured the bot, you can run the bot with the following command:

```bash
python bot.py
```

Ensure that the `config.json` file is properly set up with your bot's token and desired command prefix.

## Commands

### !ping
- **Description**: Shows the bot's current latency.
- **Usage**: `!ping`

### !kick <user> [reason]
- **Description**: Kicks a user from the server with an optional reason.
- **Usage**: `!kick @username [reason]`
- **Permissions Required**: `kick_members`

### !clear <number>
- **Description**: Deletes a specified number of messages from the current channel (max 50).
- **Usage**: `!clear 10`
- **Permissions Required**: `administrator`

### !sw <id>
- **Description**: Fetches information about a Star Wars character based on their ID.
- **Usage**: `!sw 2` (returns information about C-3PO)

### !help
- **Description**: Displays the list of available commands and their usage.
- **Usage**: `!help`


## Creating Custom Commands

To add new commands, you can create a new `.py` file inside the `cogs/` folder. Here’s an example of how to add a simple command to the bot:

```python
import discord
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello, world!")

async def setup(bot):
    await bot.add_cog(Example(bot))
```

Save the file as `example.py` in the `cogs/` folder, then add `cogs.example` to the `initial_extensions` list in `bot.py`.

## Contribution

Feel free to contribute to this project by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License.

---
