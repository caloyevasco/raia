from discord.ext import commands

class Basic_Player_Commands(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="truckkun")
	async def truckkun(self,ctx):
		discord_id = str(ctx.author.id)
		await ctx.send(f"{ctx.author.mention}-{discord_id} you have been reincarnated, this will put the player in the database.(test)")


def setup(bot):
	bot.add_cog(Basic_Player_Commands(bot))