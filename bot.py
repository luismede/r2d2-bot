import discord, json, asyncio
from discord.ext import commands

with open('config/config.json') as config_file:
  config = json.load(config_file)


intents = discord.Intents.all()
intents.message_content = True

activity = discord.Activity(type=discord.ActivityType.watching, name="!h")
client = commands.Bot(command_prefix=config['prefix'], activity=activity, status=discord.Status.do_not_disturb, intents=intents)

initial_extensions = ['cogs.ping', 'cogs.kick', 'cogs.clear', 'cogs.swapi', 'cogs.help']

async def load_cogs():
  for extension in initial_extensions:
    try:
      await client.load_extension(extension)
      print(Color.green + f'Loaded extension {extension}' + Color.reset_all)
    except Exception as e:
      print(Color.red + f'Failed to load extension {extension}! Error: {e}' + Color.reset_all)

class Color:
  green='\033[32m'
  red='\033[31m'
  reset_all='\033[0;0m'

  
@client.event
async def on_ready():
  print(Color.green + f'Logged on as {client.user}' + Color.reset_all)

if __name__ == '__main__':
  asyncio.run(load_cogs())
  client.run(config['token'])