import market_database_tool
from discord.ext import commands
import raia

class MarketCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.command(name='checkitem')
	async def checkitem(self, ctx, item_name_arg):
		check = raia.player_system.get_player_by_id(ctx.author.id)
		if check == None:
			await ctx.send(f"Hello there {ctx.author.mention} you cannot use any other commands because you are not yet in the game, type \"r/budgetme \" to get started.")
			return
		item = raia.market_system.get_item_by_name(str(item_name_arg))
		await ctx.send(f"item id : {item.item_id}\nitem name : {item.item_name}\nitem price :  {item.item_price}")
		return
	

	@commands.command(name='shop')
	async def shop(self, ctx):
		check = raia.player_system.get_player_by_id(ctx.author.id)
		if check == None:
			await ctx.send(f"Hello there {ctx.author.mention} you cannot use any other commands because you are not yet in the game, type \"r/budgetme \" to get started.")
			return
		raia.cache_items()
		msg = ""
		for key, value in raia.list_all_items():
			msg+=f"{key}:{value}\n"
		await ctx.send(msg)


	@commands.command(name='buy')
	async def buy(self, ctx, item_name):
		check = raia.player_system.get_player_by_id(ctx.author.id)
		if check == None:
			await ctx.send(f"Hello there {ctx.author.mention} you cannot use any other commands because you are not yet in the game, type \"r/budgetme \" to get started.")
			return
		check_item = raia.market_system.get_item_by_name(str(item_name))
		if check_item != None:
			await ctx.send(f"{ctx.author.mention} bought {check_item.item_name} for {check_item.item_price}")
		else:
			return


def setup(bot):
	bot.add_cog(MarketCommands(bot))