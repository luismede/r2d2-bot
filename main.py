import discord, os
from discord.ext import commands
from dotenv import load_dotenv

import requests

load_dotenv()

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

blue = 0x992d22

@client.event
async def on_ready():
  print(f'Logged on as {client.user}!')

@client.command()
async def hello(ctx):
  await ctx.send(f"Hello, I'm {client.user}")
  

@client.command()
async def sw(ctx:commands.Context, id):
  base_url = 'https://swapi.dev/api/people/'
  
  response_base = requests.get(f'{base_url + id}')
  
  if response_base.status_code == 404:
    await ctx.send(f'People {id} not found. Try between 1 and 83')
  else:
    x = response_base.json()
    response_home = requests.get(x['homeworld'])
    y = response_home.json()
    embed = discord.Embed(title='Star Wars Peoples', color=discord.Color.blue())
    embed.add_field(name='Name: ', value=f'{x["name"]}', inline=True)
    embed.add_field(name='Height (cm): ', value=f'{x["height"]}', inline=True)
    embed.add_field(name='Gender: ', value=f'{x["gender"]}', inline=True)
    embed.add_field(name='Birth Year: ', value=f'{x["birth_year"]}', inline=True)
    embed.add_field(name='HomeWorld: ', value=f'{y["name"].capitalize()}', inline=True)
    await ctx.send(embed=embed)
    
@commands.has_permissions(administrator=True)
@client.command()
async def clear(ctx, messages:int):
  if messages > 50:
    messages = 50
    return await ctx.send("You can't clear more than 50 messages at once!")
  await ctx.channel.purge(limit=messages + 1)

client.run(os.getenv("SECRET_TOKEN"))