import discord

class Startup(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("creating table")
		dbt.create_table()


def setup(bot):
    bot.add_cog(Startup(bot))
