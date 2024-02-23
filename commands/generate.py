

import discord, random, requests 
from essential.load_user_groups import load_user_groups
from discord.ext import commands


def setup(bot):
    @bot.tree.command(name="generate_img", description="Generate Random Images")
    async def generate_img(interaction: discord.Interaction, num_images: int = 1):
        user_id = interaction.user.id
        user_groups = load_user_groups()

        if user_id in user_groups["admins"] or user_id in user_groups["vips"] or num_images <= 5:
            mention = interaction.user.mention
            
            await interaction.response.send_message(content=f"{mention} Generating {num_images} images...", ephemeral=True)

            for _ in range(num_images):
                random_size = random.randrange(1080)
                url = f'https://picsum.photos/{random_size}'

                response = requests.get(url)
                if "Invalid size" in response.text:
                    # If invalid size, continue loop without sending a response
                    continue
                else:
                    # Generate a random color for the embed
                    random_color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                    embed = discord.Embed(title="Generated Image", color=random_color)
                    embed.set_image(url=url)
                    await interaction.followup.send(content=f"{mention} Here is your generated image:", embed=embed)
                    
                     

            # Notify the user after generating all images
            await interaction.followup.send(content=f"{mention} Successfully generated {num_images} images.")
        else:
            mention = interaction.user.mention
            await interaction.response.send_message(content=f"{mention} You are not allowed to generate more than 5 images at once.", ephemeral=True)
            