from essential.load_user_groups import load_user_groups
import discord, requests, random
from discord.ext import commands
def setup(bot):

    # Giphy API defaults
    giphy = {
        "baseURL": "https://api.giphy.com/v1/gifs/",
        "apiKey": "0UTRbFtkMxAplrohufYco5IY74U8hOes",
        "tags": ["fail", "funny","hilarious", "prank", "oops", "meme", "laughter", "comedy", "epicfail", "lol", "humor", "clumsy", "accident", "silly", "facepalm", "giggle", "laughtertherapy", "rofl", "awkward", "fall", "slip", "mishap", "bloopers", "unlucky", "chuckle", "whooops", "muff", "haha", "gaffe", "gigglefest", "misstep", "lighthearted", "comic", "funnymoments", "laughsfordays", "mirth", "ridiculous", "Kurds", "Kurdistan", "KurdishMilitary", "Peshmerga", "KurdishCulture", "KurdishDance", "KurdishFood", "KurdishHistory", "KurdishTradition", "KurdishLanguage", "Rojava"],
        "type": "random",
        "rating": "r",  # Set to "r" for NSFW content
    }
    random_tag = random.choice(giphy['tags'])
    # Giphy API URL
    giphyURL = (
        f"{giphy['baseURL']}{giphy['type']}?api_key={giphy['apiKey']}&tag={random_tag}&rating={giphy['rating']}")

     
    @bot.tree.command(name="generate_gif", description="Generate Random GIFs")
    async def generate_gif(interaction: discord.Interaction, num_gifs: int = 1):
        user_id = interaction.user.id
        user_groups = load_user_groups()

        if user_id in user_groups["admins"] or user_id in user_groups["vips"] or num_gifs <= 5:

            mention = interaction.user.mention
            await interaction.response.send_message(content=f"{mention} Generating {num_gifs} GIFs...", ephemeral=True)

            for _ in range(num_gifs):
                try:
                    response = requests.get(giphyURL)
                    response.raise_for_status()  # Raise an HTTPError for bad responses
                    gif_data = response.json()

                    # Get the original gif URL
                    gif_url = gif_data["data"]["images"]["original"]["url"]

                    # Generate a random color for the embed
                    random_color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                    # Create an embed with the gif
                    embed = discord.Embed(title="Random GIF", color=random_color)
                    embed.set_image(url=gif_url)

                    await interaction.followup.send(content=f"{mention} Here is your generated GIF:", embed=embed)

                except requests.RequestException as e:
                    print(f"Error fetching Giphy data: {e}")
                    await interaction.followup.send(content=f"{mention} Oops! Something went wrong while fetching a random GIF.", ephemeral=True)

            # Notify the user after generating all GIFs
            await interaction.followup.send(content=f"{mention} Successfully generated {num_gifs} GIFs.")
        else:
            mention = interaction.user.mention
            await interaction.response.send_message(content=f"{mention} You are not allowed to generate more than 5 GIFs at once.", ephemeral=True)


    
