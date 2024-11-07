import discord
from discord.ext import commands
from discord.ext.commands import CheckFailure

class Kick(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(pass_context=True, name='kick')
  @commands.has_permissions(manage_roles=True, kick_members=True)
  async def kick(self, ctx, member: discord.Member=None, *, reason=None):
    if member is None:
      await ctx.send('You need mention a user for kick!')
      return
  
    try:
      await member.send(f'You have been kicked from the server by {ctx.author.name}. Reason: {reason if reason else "No reason specified."}')
    except discord.Forbidden:
      await ctx.send(f'I was unable to send a private message to {member.name}. ')
      
      
    await member.kick(reason=reason)
    await ctx.send(member.mention + ' was kicked from the server')
    
  @kick.error
  async def kick_error(self, ctx, error):
    if isinstance(error, CheckFailure):
      await ctx.send("You don't have permission to do this.")
  
async def setup(bot):
  await bot.add_cog(Kick(bot))