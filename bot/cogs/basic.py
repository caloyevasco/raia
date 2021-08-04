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
						await main_channel.send(content = "@everyone I am online, changes have been made.", allowed_mentions = discord.AllowedMentions(everyone = True))


	@commands.command(name='stats')
	async def stats(self, ctx):
		stats = main.player_commands.checks_stats(ctx)
		if stats != False:
			embed = discord.Embed(title=f"Status of {str(stats.player_name)}")
			embed.set_author(name=str(stats.player_name), icon_url=ctx.author.avatar_url)
			embed.add_field(name=f":globe_with_meridians: **Class** : {stats.player_class}",value="`the player's class.`", inline=True)
			embed.add_field(name=f":bust_in_silhouette:**Race** : {stats.player_race}",value="`the player's race`", inline=True)
			embed.add_field(name=f":heart: **Health Points** : {stats.player_health}",value="`the player's health points.`", inline=False)
			embed.add_field(name=f":mechanical_arm: **Physical Potential** : {stats.player_attack}",value="`how dangerous you are.`", inline=False)
			embed.add_field(name=f":stars: **Magic Potential** : {stats.player_attack}",value="`how dangerous you are, hypothetically.`", inline=False)
			embed.add_field(name=f":shield: **Defensive Potential** : {stats.player_defense}",value="`how sturdy you are`", inline=False)
			await ctx.send(embed=embed)
		elif stats == False:
			await ctx.send(f"{ctx.author.mention} you must join the game by typing `r/join` before you can use any other commands that this bot provides.")
		else:
			pass


	@commands.command(name='inventory')
	async def inventory(self, ctx):
		inv = main.player_commands.checks_inventory(ctx)
		if inv != False:
			await ctx.send(embed=inv)
		else:
			await ctx.send(f"{ctx.author.mention} you must join the game by typing `r/join` before you can use any other commands that this bot provides.")
		


	@commands.command(name="join")
	async def join(self,ctx):
		joins = main.player_commands.new_player(ctx)
		if joins == True:
			await ctx.send(f"A Light suck you in the air! You've been Transmigrated in another World! Welcome to Raia, {ctx.author.mention}!")
		elif joins == False:
			await ctx.send(f"You have been already Transmigrated to Raia {ctx.author.mention}!")


def setup(bot):
	bot.add_cog(Basic_Player_Commands(bot))

