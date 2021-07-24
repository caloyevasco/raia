class Item(object):
	def __init__(self, item_id, item_name, item_price):
		self.item_id = item_id
		self.item_name = item_name
		self.item_price = item_price


class MarketBase(object):


	def __init__(self, ValueBase, SqliteDatabaseTool, item_dataset, database_dataset, stringtools, base_dataset):
		self.SqliteDatabaseTool = SqliteDatabaseTool
		self.ValueBase = ValueBase(self.SqliteDatabaseTool, database_dataset, item_dataset, base_dataset, stringtools)
		self.item_dataset = item_dataset
		self.database_dataset = database_dataset
		self.stringtools = stringtools
		self.base_dataset = base_dataset


	def add_item(self, item_id_arg, item_name_arg, item_price_arg):
		if self.get_item_by_id(item_id_arg) == None:
			self.SqliteDatabaseTool.exec_commit(f"INSERT INTO {self.database_dataset['table_name']} VALUES ({item_id_arg}, {self.stringtools.text(item_name_arg)}, {item_price_arg})")
			return
		else:
			print("item already exists")
		return


	def get_item_by_name(self, item_name_arg):
		item = self.SqliteDatabaseTool.exec_fetchone(f"SELECT * FROM {self.database_dataset['table_name']} WHERE {self.item_dataset['item_name']}=={self.stringtools.text(item_name_arg)} ")
		if item != None:
			item_id, item_name, item_price = item
			return Item(item_id, item_name, item_price)
		else:
			return None


	def get_all_items(self):
		return self.SqliteDatabaseTool.exec_fetchall(f"SELECT * FROM {self.database_dataset['table_name']}")


	def get_item_by_id(self, item_id_arg):
		item = self.SqliteDatabaseTool.exec_fetchone(f"SELECT * FROM {self.database_dataset['table_name']} WHERE {self.item_dataset['item_id']}=={item_id_arg} ")
		if item != None:
			item_id, item_name, item_price = self.SqliteDatabaseTool.exec_fetchone(f"SELECT * FROM {self.database_dataset['table_name']} WHERE {self.item_dataset['item_id']}=={item_id_arg} ")
			return Item(item_id, item_name, item_price)
		else:
			return None


	def get_all_items(self):
		return [Item(item_id, item_name, item_price) for item_id, item_name, item_price in self.SqliteDatabaseTool.exec_fetchall(f"SELECT * FROM {self.database_dataset['table_name']}")]


	def get_item_by_price(self, item_gold_arg):
		return [Item(item.item_id, item.item_name, item.item_price) for item in self.SqliteDatabaseTool.exec_fetchall(f"SELECT * FROM {self.database_dataset['table_name']} WHERE {self.item_dataset['item_price']}=={self.stringtools.text(item_gold_arg)} ")]


class MarketDatabaseTool(MarketBase):


	def __init__(self, db_dir, ValueBase, SqliteDatabaseTool, item_dataset, database_dataset, stringtools, base_dataset):
		self.SqliteDatabaseTool = SqliteDatabaseTool(db_dir)
		super().__init__(ValueBase, self.SqliteDatabaseTool, item_dataset, database_dataset, stringtools, base_dataset)
		self.item_dataset = item_dataset
		self.memory_cache = []

	def create_table(self, command_format):
		self.SqliteDatabaseTool.exec(command_format)
		return

	def cache_items(self):
		for item in self.get_all_items():
			self.memory_cache.append(item)


	def list_all_items(self):
		items = []
		if self.memory_cache == []:
			return None
		for item in self.memory_cache:
			items.append({self.item_dataset['item_name']:item.item_name, self.item_dataset['item_price']:item.item_price})
			return items
