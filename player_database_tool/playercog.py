import discord
from discord.ext import commands
import player_database_tool
import run

class PlayerCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.command(name="budgetme")
	async def budget(self, ctx):
		check = run.player_system.get_player_by_id(ctx.author.id)
		if check == None:
			run.player_system.new_player(ctx.author.id, str(ctx.author.name), 1000)
			await ctx.send(f"Hello there {ctx.author.mention} here is 1000 to get you started!")
		else:
			return
	
	@commands.command(name="stat")
	async def status(self, ctx, other_playername_arg=None):
		check = run.player_system.get_player_by_id(ctx.author.id)
		if check == None:
			await ctx.send(f"Hello there {ctx.author.mention} you cannot use any other commands because you are not yet in the game, type \"r/budgetme \" to get started.")
			return
		player = run.player_system.get_player_by_id(ctx.author.id)
		await ctx.send(f"stats:\nplayer name:{player.player_name}\nplayer gold:{player.player_gold}")


def setup(bot):
	bot.add_cog(PlayerCommands(bot))