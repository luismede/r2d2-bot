import discord
from discord.ext import commands
from datetime import datetime

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='h', h="Show available commands")
    async def help(self, ctx):
        embed = discord.Embed(
            title='Help Command',
            description='List of available commands and their usage',
            timestamp=datetime.now(),
            color=discord.Color.blue()
        )
        
        embed.add_field(name='Prefix: ', value=f'!', inline=True)
        embed.add_field(name='help: ', value=f'Show commands', inline=True)
        embed.add_field(name='kick <user>: ', value=f'Kicks a member from the server', inline=False)
        embed.add_field(name='ping: ', value=f'Shows the bot\'s latency', inline=False)
        embed.add_field(name='sw <id>: ', value=f'Shows information about a Star Wars character (Ex.: !sw 2)', inline=False)
        embed.add_field(name='clear <number>: ', value=f'Clears a specified number of messages', inline=False)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
