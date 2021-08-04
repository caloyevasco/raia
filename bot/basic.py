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
			else:
				for channel in guild.text_channels:
					if channel.name == bots_channel:
						main_channel = self.bot.get_channel(channel.id)
						await main_channel.send(content = "@everyone I am online.", allowed_mentions = discord.AllowedMentions(everyone = True))


	@commands.command(name='stats')
	async def stats(self, ctx):
		stats = main.player_commands.checks_stats(ctx)
		embed = discord.Embed(title=f"Status of {str(stats.player_name)}")
		embed.set_author(name=str(stats.player_name), icon_url=ctx.author.avatar_url)
		embed.add_field(name=f"player class : {stats.player_class}",value="the player's class", inline=True)
		embed.add_field(name=f"player health : {stats.player_health}",value="the player's health points", inline=False)
		embed.add_field(name=f"player attack : {stats.player_attack}",value="how dangerous you are", inline=False)
		embed.add_field(name=f"player defense : {stats.player_defense}",value="how sturdy you are", inline=False)
		await ctx.send(embed=embed)

	@commands.command(name="join")
	async def join(self,ctx):
		joins = main.player_commands.new_player(ctx)
		if joins == False:
			await ctx.send(f"A Light suck you in the air! You've been Transmigrated in another World! Welcome to Raia, {ctx.author.mention}!")
		else:
			await ctx.send(f"A Light suck you in the air! You've been Transmigrated in another World! Welcome to Raia, {ctx.author.mention}!")


def setup(bot):
	bot.add_cog(Basic_Player_Commands(bot))