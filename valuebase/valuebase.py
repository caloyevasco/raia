from stringtools import stringtools
class ValueBase(object):


	def __init__(self, SqliteDatabaseTool, value_database_dataset, value_dataset, base_dataset, stringtools):
		self.SqliteDatabaseTool = SqliteDatabaseTool
		self.value_database_dataset = value_database_dataset
		self.value_dataset = value_dataset
		self.base_dataset = base_dataset
		self.stringtools = stringtools

	def get_value_by_name(self, value_name_arg):
		return self.SqliteDatabaseTool.exec_fetchone(f"SELECT * FROM {self.value_database_dataset['table_name']} WHERE {self.base_dataset['name']}=={self.stringtools.text(value_name_arg)}")


	def get_value_by_id(self, value_id_arg):
		return self.SqliteDatabaseTool.exec_fetchone(f"SELECT * FROM {self.value_database_dataset['table_name']} WHERE {self.base_dataset['id']}=={self.stringtools.text(value_id_arg)}")


	def by_id_change_value_name(self, value_id_arg, new_name_arg):
		self.SqliteDatabaseTool.exec_commit(f"UPDATE {self.value_database_dataset['table_name']} SET {self.value_dataset['name']} = {new_playername_arg} WHERE {self.value_dataset['id']}=={value_id_arg}")
		return

