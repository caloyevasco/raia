from databasetool.databasetool import DatabaseTool
import discord


#Item dictionary
class ItemDict(object):


	def __init__(self):
		pass


	def parse_item(self, item_dict):
		self.item_name = item_dict['item_name']
		self.item_type = item_dict['item_type']
		self.item_description = item_dict['item_description']
		self.item_amount = item_dict['item_amount']


	def create_item(self, item_name, item_type, item_amount, item_description):
		return {
			"item_name":item_name,
			"item_type":item_type,
			"item_amount":item_amount,
			"item_description":item_description
				}
	

	def deduct_amount(self, amount=1):
		if ammount < 0:
			return "amount cannot be zero."
		elif amount < 0 and self.item:
			pass


class PlayerDict(object):


	def __init__(self, context=None):
		self.context = context


	def create(self) -> dict:
		starter_item = ItemDict()
		coins = starter_item.create_item("iron coins", "currency", 50, "make us multiply!")
		return	{str(self.context.author.id):
					{
										"player_information":{
																	"player_name":self.context.author.name,
																	"player_id":self.context.author.id
															},

										"player_stats":	{
															"player_class":"None",
															"player_race":"None",
															"player_health":20,
															"player_attack":1,
															"player_defense":1
														},


										"player_inventory":[coins]
					}
				}
	

	def parse(self, player_dict) -> object:
		self.player_name = player_dict["player_information"]["player_name"]
		self.player_id = player_dict["player_information"]["player_id"]
		self.player_class = player_dict["player_stats"]["player_class"]
		self.player_race = player_dict["player_stats"]["player_race"]
		self.player_health = player_dict["player_stats"]["player_health"]
		self.player_attack = player_dict["player_stats"]["player_attack"]
		self.player_defense = player_dict["player_stats"]["player_defense"]
		self.player_inventory = player_dict["player_inventory"]
		return


	def get_inventory(self):
		""" returns a list of dictionaries.a """
		return self.player_inventory


	def append_to_inventory(self, item_dict):
		self.get_inventory.append(item_dict)


class Check(object):

	def __init__(self, text_channel_name):
		self.text_channel_name = text_channel_name
		self.db_tool = DatabaseTool('bot/database.json')


	def check_player(self, ctx):
		def _outer_callable_(func):
			def _inner_callable_(*args):
				if self.db_tool.get(ctx.author.id):
					return False
				else:
					return func(args)
			return _inner_callable_
		return _outer_callable_


	def check_channel(self, ctx):
		def _outer_callable_(func):
			def _inner_callable_(*args):
				if ctx.channel.name == self.text_channel_name:
					return func(args)
				else:
					return False
			return _inner_callable_
		return _outer_callable_
	

class MemberCommands(object):


	def __init__(self, text_channel_name):
		self.text_channel_name = text_channel_name


class PlayerCommands(Check, MemberCommands):


	def __init__(self, text_channel_name):
		Check.__init__(self, text_channel_name)
		self.db_tool = DatabaseTool('bot/database.json')


	def new_player(self, context):
		""" Creates a new player in the database """
		@Check.check_channel(self, context)
		@Check.check_player(self, context)
		def new_player_func(*args):
			#creates player
			new_player_var = PlayerDict(context)
			self.db_tool.create(new_player_var.create())
			return f"A Light suck you in the air! You've been Transmigrated in another World! Welcome to Raia, {context.author.mention}!"
		checked = new_player_func()
		if checked:
			return checked
		else:
			return f"You have been already Transmigrated to Raia {context.author.mention}!"


	def checks_stats(self, context):
		@Check.check_channel(context)
		@Check.check_player(context)
		def checks_stats_func(*args):
			player = self.db_tool.get(context.author.id)
			if player != False:
				player_dict = PlayerDict()
				player_dict.create(player)
				return player_dict
			else:
				return False
		checks_stats_func()


	def checks_inventory(self, context):
		@Check.check_channel(context)
		@Check.check_player(context)
		def checks_inventory_func(*args):
			player = self.db_tool.get(context.author.id)
			if player != False:
				player_dict = PlayerDict()
				item_dict = ItemDict()
				player_dict.create(player)
				embed = embed = discord.Embed(title=f"Inventory of {str(player_dict.player_name)}")
				embed.set_author(name=str(player_dict.player_name), icon_url=context.author.avatar_url)
				for item in player_dict.get_inventory():
					embed.add_field(name=f"**{item['item_name']} : {item['item_amount']}**", value=f"*{item['item_description']}*")
				return embed
			else:
				return False
		checks_stats_func()