import discord
import discord.utils
from discord.ext import commands
from database_tools.databasetool import DataBaseTool


dbt = DataBaseTool("users.db")


class Transactions(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(name='budgetme')
	async def givebudget(self, ctx):
		dbt.write(ctx.author.id, ctx.author.name, 1000)
		await ctx.send(f"1000 sent to {ctx.message.author.mention}")


	@commands.command(name='give')
	async def give(self, ctx, name):
		self.member = discord.utils.get(self.bot.get_all_members(), name=name, discriminator="discriminator")


		if self.member != None:
			await ctx.send(f"{ctx.author.mention} sends something to {self.member}")
		else:
			await ctx.send(f"{ctx.author.mention}, too bad the user {name} could not be found in this server.")


	@commands.command(name='bal')
	async def balance(self, ctx):
		user = dbt.get(ctx.author.id)
		await ctx.send(f"{user.user_name} has {user.gold}")


def setup(bot):
    bot.add_cog(Transactions(bot))

