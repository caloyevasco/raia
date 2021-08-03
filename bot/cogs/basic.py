from discord.ext import commands
from databasetool.databasetool import DatabaseTool

class Basic_Player_Commands(commands.Cog):


	def __init__(self, bot):
		self.bot = bot


	@commands.command(name="truckkun")
	async def truckkun(self,ctx):
		discord_id = str(ctx.author.id)
		discord_name = str(ctx.author.name)
		database = DatabaseTool(discord_id, "bot/database.json")
		if database.create({discord_id:{"player_name":discord_name}}):
			await ctx.send(f"\"`A Light suck you in the air! You've been Transmigrated in another World! Welcome to Raia {ctx.author.mention}!`\"")
		else:
			await ctx.send(f"You have been already Transmigrated to Raia {ctx.author.mention}.")
	
	


def setup(bot):
	bot.add_cog(Basic_Player_Commands(bot))