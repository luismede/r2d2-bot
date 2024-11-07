import aiohttp
import discord
from discord.ext import commands
from datetime import datetime
import asyncio

class StarWars(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def fetch_data(self, session, url):
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            return None

    @commands.command(name='sw')
    async def sw(self, ctx, id: int):
        base_url = f'https://swapi.dev/api/people/{id}/'
        
        async with aiohttp.ClientSession() as session:
            person_data = await self.fetch_data(session, base_url)
            
            if person_data is None:
                await ctx.send(f'Character with ID {id} not found.')
                return

            homeworld_data = await self.fetch_data(session, person_data['homeworld'])
            homeworld_name = homeworld_data['name'].capitalize() if homeworld_data else 'Unknown'
            
            films_tasks = [self.fetch_data(session, film_url) for film_url in person_data['films']]
            films_data = await asyncio.gather(*films_tasks)

            films = [film['title'] for film in films_data if film]

            embed = discord.Embed(title='Wiki Peoples', timestamp=datetime.now(), color=discord.Color.blue())
            embed.add_field(name='Name: ', value=f'{person_data["name"]}', inline=True)
            embed.add_field(name='Height (cm): ', value=f'{person_data["height"]}', inline=True)
            embed.add_field(name='Mass: ', value=f'{person_data["mass"]}', inline=True)
            embed.add_field(name='Gender: ', value=f'{person_data["gender"]}', inline=True)
            embed.add_field(name='Birth Year: ', value=f'{person_data["birth_year"]}', inline=True)
            embed.add_field(name='HomeWorld: ', value=f'{homeworld_name}', inline=True)
            embed.add_field(name='Films: ', value=', '.join(films) if films else 'No films found', inline=False)

            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(StarWars(bot))
