class Player(object):


	def __init__(self, player_id_arg, player_name_arg, player_gold_arg):
		self.player_id= player_id_arg
		self.player_name = player_name_arg
		self.player_gold = player_gold_arg


class PlayerDatabaseBase(object):


	def __init__(self, db_dir, ValueBase, SqliteDatabaseTool, player_dataset, database_dataset,stringtools, base_dataset):
		self.SqliteDatabaseTool = SqliteDatabaseTool(db_dir)
		self.ValueBase = ValueBase(self.SqliteDatabaseTool, database_dataset, player_dataset, base_dataset, stringtools)
		self.player_dataset = player_dataset
		self.database_dataset = database_dataset
		self.stringtools = stringtools


	def add_player(self, player_id_arg, player_name_arg, player_gold_arg):
		if self.get_player_by_id(player_id_arg) == None:
			self.SqliteDatabaseTool.exec_commit(f"INSERT INTO {self.database_dataset['table_name']} VALUES ({player_id_arg}, {self.stringtools.text(player_name_arg)}, {player_gold_arg})")
			return
		else:
			pass
		return


	def get_player_by_name(self, player_name_arg, /):
		plyr = self.ValueBase.get_value_by_id(player_name_arg)
		if plyr != None:
			player_id, player_name, player_gold = plyr
			return Player(player_id, player_name, player_gold)
		else:
			return None


	def get_player_by_id(self, player_id_arg, /):
		plyr = self.ValueBase.get_value_by_id(player_id_arg)
		if plyr != None:
			player_id, player_name, player_gold = plyr
			return Player(player_id, player_name, player_gold)
		else:
			return None


	def get_player_by_gold(self, player_gold_arg, /):
		return [Player(player_id, player_name, player_gold) for player_id, player_name, player_gold in self.SqliteDatabaseTool.exec_fetchall(f"SELECT * FROM {self.database_dataset['table_name']} WHERE {self.player_dataset['player_gold']}=={self.stringtools.text(player_gold_arg)} ")]



	def by_id_add_player_gold(self, player_id_arg, total_gold_arg, /):
		self.SqliteDatabaseTool.exec_commit(f"UPDATE {self.database_dataset['table_name']} SET {self.player_dataset['player_gold']} = {self.player_dataset['player_gold']} + {total_gold_arg} WHERE {self.player_dataset['player_id']}=={player_id_arg}")
		return


	def by_name_add_player_gold(self, player_name_arg, total_gold_arg, /):
		self.SqliteDatabaseTool.exec_commit(f"UPDATE {self.database_dataset['table_name']} SET {self.player_dataset['player_gold']} = {self.player_dataset['player_gold']} + {total_gold_arg} WHERE {self.player_dataset['player_name']}=={self.stringtools.text(player_name_arg)}")
		return


	def by_id_deduct_player_gold(self, player_id_arg, total_gold_arg, /):
		self.SqliteDatabaseTool.exec_commit(f"UPDATE {self.database_dataset['table_name']} SET {self.player_dataset['player_gold']} = {self.player_dataset['player_gold']} - {total_gold_arg} WHERE {self.player_dataset['player_id']}=={player_id_arg}")
		return


	def by_name_deduct_player_gold(self, player_name_arg, total_gold_arg, /):
		self.SqliteDatabaseTool.exec_commit(f"UPDATE {self.database_dataset['table_name']} SET {self.player_dataset['player_gold']} = {self.player_dataset['player_gold']} - {total_gold_arg} WHERE {self.player_dataset['player_name']}=={self.stringtools.text(player_name_arg)}")
		return


	def by_id_update_player_name(self, player_id_arg, new_playername_arg, /):
		self.data_base_conn.exec_commit(f"UPDATE {self.database_dataset['table_name']} SET {self.database_dataset['player_name']} = {new_playername_arg} WHERE {self.player_dataset['player_id']}=={player_id_arg}")
		return


class PlayerDatabaseTool(PlayerDatabaseBase):


	def __init__(self, db_dir, ValueBase, SqliteDatabaseTool, player_dataset, database_dataset, stringtools, base_dataset):
		super().__init__(	
							db_dir=db_dir,
							ValueBase=ValueBase,
							SqliteDatabaseTool=SqliteDatabaseTool,
							player_dataset=player_dataset,
							database_dataset=database_dataset,
							stringtools=stringtools,
							base_dataset=base_dataset
						)


	def create_table(self, command):
		self.SqliteDatabaseTool.exec(command)
		return


	def new_player(self, player_id_arg, player_name_arg, player_gold_arg):
		self.add_player(player_id_arg, player_name_arg, player_gold_arg)
		return
