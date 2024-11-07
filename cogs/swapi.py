import discord, requests, datetime
from discord.ext import commands

class Swapi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command(name='sw')
    async def sw(self, ctx, id):
      films = list()
      
      base_url = 'https://swapi.dev/api/people/'
      response_base = requests.get(f'{base_url + id}')
      
      if response_base.status_code == 404:
        await ctx.send(f'People {id} not found. Try between 1 and 83')
      else:
        x = response_base.json()
        response_home = requests.get(x['homeworld'])
        y = response_home.json()
        for filmes in x['films']:
          response_films = requests.get(filmes)
          z = response_films.json()
          films.append(z['title'])
          
        embed = discord.Embed(title='Wiki Peoples', timestamp=datetime.datetime.now(), color=discord.Color.blue())
        embed.add_field(name='Name: ', value=f'{x["name"]}', inline=True)
        embed.add_field(name='Height (cm): ', value=f'{x["height"]}', inline=True)
        embed.add_field(name='Gender: ', value=f'{x["gender"]}', inline=True)
        embed.add_field(name='Birth Year: ', value=f'{x["birth_year"]}', inline=True)
        embed.add_field(name='HomeWorld: ', value=f'{y["name"].capitalize()}', inline=True)
        embed.add_field(name='Mass: ', value=f'{x["mass"]}', inline=True)

      embed.add_field(name='Films: ', value=f'{', '.join(films)}', inline=True)
      await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Swapi(bot))
