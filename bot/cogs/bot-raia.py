from discord.ext import commands
import discord
from databasetool.databasetool import DatabaseTool

class (commands.Cog):


	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_ready(self):
		bots_channel = "raia-main"
		for guild in self.bot.guilds:
			if bots_channel not in [channel.name for channel in guild.text_channels]:
				await guild.create_text_channel(bots_channel)


def setup(bot):
	bot.add_cog(Basic_Player_Commands(bot))