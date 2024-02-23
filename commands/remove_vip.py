

from essential.load_user_groups import load_user_groups
from essential.save_user_groups import save_user_groups
import discord
from discord.ext import commands

def setup(bot):
    @bot.tree.command(name="remove_vip", description="Remove user from VIP group")
    async def remove_vip(interaction: discord.Interaction, user: discord.User):
        user_groups = load_user_groups()

        if interaction.user.id in user_groups["admins"]:
            if user.id in user_groups["vips"]:
                user_groups["vips"].remove(user.id)
                save_user_groups(user_groups)
                await interaction.response.send_message(content=f"{user.mention} has been removed from the VIP group.", ephemeral=True)
            else:
                await interaction.response.send_message(content=f"{user.mention} is not in the VIP group.", ephemeral=True)
        else:
            await interaction.response.send_message(content="You do not have permission to remove users from the VIP group.", ephemeral=True)
