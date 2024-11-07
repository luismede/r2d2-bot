from discord.ext import commands

class Ping(commands.Cog):
  def __init__(self, bot):
      self.bot = bot
      super().__init__()

  @commands.command(name='ping')
  async def ping(self, ctx):
    latency = round(self.bot.latency * 1000)
    await ctx.send(f'Pong! In {latency}ms')

async def setup(bot):
  await bot.add_cog(Ping(bot))

