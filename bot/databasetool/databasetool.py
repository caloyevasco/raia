import json


def load_database(database):
	""" Opens the database """
	with open(database) as file:
		return json.load(file)


class DatabaseTool():

	"""
		DATE: AUGUST 2, 2021
		NOTE: THIS ONLY WORKS TO THE USER, WHICH MEANS THAT YOU CANNOT CHECK OTHER PLAYERS ACCOUNTS, ONLY THYSELF.

		__init__(self, playerid, database)
			playerid - this arument should take the id of the user who is using this class's attributes and methods.
			database - this argument takes the database file name path.

		get(self) -> returs a dictionary of player information inside the databse json file.
		create(self) - creates a user in the database if the user does not yet exist inside the database.
	"""

	def __init__(self, playerid, database):
		self.database_file = database
		self.database_object = load_database(database)


	def get(self, playerid):
		""" uses the self.database_object to check if the user id already exists inside the database. """
		#loads the self.database_object -> dict
		record = self.database_object
		self.userid = str(playerid)

		if record.get(str(self.userid)):
			return record[str(self.userid)]
		else:
			return


	def create(self, player_dict):
		""" creates a player inside the databse is the player is not in the database yet. """
		if self.get(list(player_dict.keys())[0]):
			return False
		else:
			cache_db = self.database_object
			cache_db[self.userid] = list(player_dict.values())[0]
			with open(self.database_file, "w") as db_f:
				json.dump(cache_db, db_f, indent="\t\t")
			return True