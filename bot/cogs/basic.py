import discord
from discord.ext import commands
import main


class Basic_Player_Commands(commands.Cog):


	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_ready(self):
		bots_channel = "raia-main"
		for guild in self.bot.guilds:
			if bots_channel not in [channel.name for channel in guild.text_channels]:
				await guild.create_text_channel(bots_channel)


	@commands.command(name="join")
	async def join(self,ctx):
		joins = main.player_commands.new_player(ctx)
		if joins:
			await ctx.send(f"\"`A Light suck you in the air! You've been Transmigrated in another World! Welcome to Raia, {context.author.mention}!`")
		else:
			await ctx.send(f"You have been already Transmigrated to Raia {context.author.mention}.")


	@commands.command(name="test")
	async def test(self, ctx):
		await ctx.send(main.process_commands.take(ctx))


def setup(bot):
	bot.add_cog(Basic_Player_Commands(bot))