import market_database_tool
from discord.ext import commands
import run

class MarketCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='checkitem')
	async def checkitem(self, ctx, item_name_arg):
		check = run.player_system.get_player_by_id(ctx.author.id)
		if check == None:
			await ctx.send(f"Hello there {ctx.author.mention} you cannot use any other commands because you are not yet in the game, type \"r/budgetme \" to get started.")
			return
		item = run.market_system.get_item_by_name(str(item_name_arg))
		await ctx.send(f"item id : {item.item_id}\nitem name : {item.item_name}\nitem price :  {item.item_price}")
	

	@commands.command(name='shop')
	async def shop(self, ctx):
		

def setup(bot):
	bot.add_cog(MarketCommands(bot))