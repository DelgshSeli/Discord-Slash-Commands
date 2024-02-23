import discord 
from essential.load_user_groups import load_user_groups
from essential.save_user_groups import save_user_groups
from discord.ext import commands

def setup(bot):
        
    @bot.tree.command(name="add_admin", description="Add user to admin group")
    async def add_admin(interaction: discord.Interaction, user: discord.User):
        user_groups = load_user_groups()

        if interaction.user.id in [413808058427244545, 388858312143405057]:
            if user.id not in user_groups["admins"]:
                user_groups["admins"].append(user.id)
                save_user_groups(user_groups)
                await interaction.response.send_message(content=f"{user.mention} has been added to the admin group.", ephemeral=True)
            else:
                await interaction.response.send_message(content=f"{user.mention} is already in the admin group." , ephemeral=True)
        else:
            await interaction.response.send_message(content="You do not have permission to add users to the admin group.", ephemeral=True)


