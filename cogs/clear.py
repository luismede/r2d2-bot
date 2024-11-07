from discord.ext import commands
from discord.ext.commands import CheckFailure

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command(pass_context=True, name='clear')
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, count:int):
        if count > 100:
          count = 100
          return await ctx.send("You can't clear more than 100 messages at once!")
        await ctx.channel.purge(limit=count + 1)
    
    @clear.error
    async def clear_error(self, ctx, error):
      if isinstance(error, CheckFailure):
        await ctx.send("You don't have permission to do this.")

async def setup(bot):
    await bot.add_cog(Clear(bot))