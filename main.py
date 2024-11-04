import discord, random
from discord.ext import commands

from secret_token import token

intents = discord.Intents.all()
client = commands.Bot(command_prefix="$", intents=intents)

@client.event
async def on_ready():
  print(f'Logged on as {client.user}!')

@client.command()
async def askme(ctx, arg):
  await ctx.send(arg)
  

async def result_integer(ctx, result):
  if result.is_integer():
    await ctx.send(f'The result is: {int(result)}')
  else:
    await ctx.send(f'The result is: {result:.2f}')
    
@client.command()
async def math(ctx, arg1: float, command:str, arg2: float):      
  match command:
    case '+':
      result = arg1 + arg2
      await result_integer(ctx, result)
    case 'x':
      result = arg1 * arg2
      await result_integer(ctx, result)
    case '-':
      result = arg1 - arg2
      await result_integer(ctx, result)
    case '/':
      result = arg1 / arg2
      await result_integer(ctx, result)
    case '//':
      result = arg1 // arg2
      await result_integer(ctx, result)
    case '**':
      result = arg1 ** arg2
      await result_integer(ctx, result)
    case _:
      print('This operation is invalid...')
client.run(token())