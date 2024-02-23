 
import discord, random
from discord.ext import commands
def setup(bot):

    @bot.tree.command(name="avatar", description="Get user avatar")
    async def avatar(interaction: discord.Interaction, member: discord.Member):
        # Generate a random color for the embed
        embed_color = discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Create an embedded message
        embed = discord.Embed(color=embed_color)

        # Use a conditional expression to set thumbnail URL based on member's avatar presence
        thumbnail_url = member.avatar.url if member.avatar else member.default_avatar.url

        # Set the thumbnail as the main content of the embed with width and height parameters
        embed.set_image(url=thumbnail_url)

        # Send the embedded message
        await interaction.response.send_message(embed=embed)




