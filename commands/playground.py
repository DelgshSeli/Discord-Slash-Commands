import discord
import requests
import random
import time

def setup(bot):
    @bot.tree.command(name="memes", description="Get a random meme")
    async def memes(interaction: discord.Interaction, tag: str = None):
        api_url = "http://kurdivan.com:4321/api/v1/random-meme"
        
        if tag:
            api_url = f"http://kurdivan.com:4321/api/v1/random-meme/tag/{tag}"
        
        # Add a timestamp or a unique identifier to force Discord to re-fetch the image
        api_url += f"?timestamp={int(time.time())}"
        
        embed = discord.Embed()
        embed.set_thumbnail(url=api_url)
        
        await interaction.response.send_message(embed=embed)
