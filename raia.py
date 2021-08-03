from market_database_tool import market_database_tool
from player_database_tool import player_database_tool
import stringtools.stringtools as strtool
from databasetool import databasetool
from datasets import datasets
from valuebase import valuebase 


mrkt_db_dtst = datasets.ITEM_DATABASE_DATASET
itm_dtst = datasets.ITEM_DATASET
plyr_db_dtst = datasets.PLAYER_DATABASE_DATASET
plyr_dtst = datasets.PLAYER_DATASET
bs_dtst = datasets.BASE_DATASET


market_db = mrkt_db_dtst['filename']
player_db = plyr_db_dtst['filename']


market_table = f"CREATE TABLE IF NOT EXISTS {mrkt_db_dtst['table_name']} ({strtool.integer_value(itm_dtst['item_id'])},{strtool.text_value(itm_dtst['item_name'])},{strtool.integer_value(itm_dtst['item_price'])})"
player_table = f"CREATE TABLE IF NOT EXISTS {plyr_db_dtst['table_name']} ({strtool.integer_value(plyr_dtst['player_id'])},{strtool.text_value(plyr_dtst['player_name'])},{strtool.integer_value(plyr_dtst['player_gold'])})"


market_system = market_database_tool.MarketDatabaseTool(	
															db_dir=market_db,
															ValueBase=valuebase.ValueBase,
															SqliteDatabaseTool=databasetool.SqliteDatabaseTool,
															item_dataset=itm_dtst,
															database_dataset=mrkt_db_dtst,
															stringtools=strtool,
															base_dataset=bs_dtst
														)


player_system = player_database_tool.PlayerDatabaseTool(	
															db_dir=player_db,
															ValueBase=valuebase.ValueBase,
															SqliteDatabaseTool=databasetool.SqliteDatabaseTool,
															player_dataset=plyr_dtst,
															database_dataset=plyr_db_dtst,
															stringtools=strtool,
															base_dataset=bs_dtst
														)


market_system.create_table(market_table)
player_system.create_table(player_table)


if __name__ == "__main__":


	player = player_database_tool.Player(200205, 'john carlo', 1000)	
	player_system.add_player(player.player_id, player.player_name, player.player_gold)
	print(f"hello {player.player_name} what do you want to do?\n\n1.shop\n2.acccount\n\n")
	def test():
		i = input("::")
		if i == 'shop' or 1:
			market_system.display_items()
			print("what do you want to buy")
			b = input("::")
			item = market_system.get_item_by_id(b)
			if item != None:
				print(f"{player.player_name} is buying {item.item_name} for {item.item_price}.")
				print("would you like to buy?")
				c = input("::")
				if c == "y":
					player_system.by_id_deduct_player_gold(player.player_id , item.item_price)
					print("trans fin.")

	x = ""

	x+="hello"
	print(x)


	print(player_system.get_player_by_id(player.player_id).__dict__)