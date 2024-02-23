import discord, os
from discord.ext import commands

from dotenv import load_dotenv
from commands.add_vip import setup as add_vip_setup
from commands.add_admin import setup as add_admin_setup
from commands.remove_admin import setup as remove_admin_setup
from commands.remove_vip import setup as remove_vip_setup
from commands.generate import setup as generate_setup
from commands.generate_gif import setup as generate_gif_setup
from commands.avatar import setup as avatar_setup
from commands.playground import setup as playground


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, activity=discord.CustomActivity('API'), status=discord.Status("dnd"))


# ===========================================================================================
add_vip_setup(bot)  # Call the setup function for add_vip command
add_admin_setup(bot)  # Call the setup function for add_admin command
remove_admin_setup(bot)  # Call the setup function for remove_admin command
remove_vip_setup(bot)  # Call the setup function for remove_vip command
generate_setup(bot)  # Call the setup function for generate command
generate_gif_setup(bot)  # Call the setup function for generate_gif command
avatar_setup(bot)  # Call the setup function for avatar command
playground(bot) # Call the setup function for testing command



@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in as {bot.user.name}')
    
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        return

    print(f"An error occurred: {error}")
    mention = ctx.author.mention
    await ctx.send(f"{mention} Oops! Something went wrong.")

load_dotenv() 
token = os.environ["TOKEN"]
bot.run(token)