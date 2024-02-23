
import discord 
from essential.load_user_groups import load_user_groups
from essential.save_user_groups import save_user_groups
from discord.ext import commands
def setup(bot):

    @bot.tree.command(name="remove_admin", description="Remove user from admin group")
    async def remove_admin(interaction: discord.Interaction, user: discord.User):
        user_groups = load_user_groups()

        if interaction.user.id in user_groups["owners"]:
            if user.id in user_groups["admins"]:
                user_groups["admins"].remove(user.id)
                save_user_groups(user_groups)
                await interaction.response.send_message(content=f"{user.mention} has been removed from the admin group.", ephemeral=True)
            else:
                await interaction.response.send_message(content=f"{user.mention} is not in the admin group." , ephemeral=True)
        else:
            await interaction.response.send_message(content="You do not have permission to remove users from the admin group.", ephemeral=True)



