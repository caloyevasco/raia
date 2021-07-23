import sqlite3


class SqliteBase(object):


	def __init__(self, db_dir):
		self._db_dir = db_dir
		self.cursor_is_open = False
		self.database_is_open = False
		self.db_connection = None
		self.db_cursor = None


	def _open_connection(self):
		self._open_database()
		self._open_cursor()


	def _close_connection(self):
		self._close_cursor()
		self._close_database()


	def _open_database(self):
		if self.database_is_open == False:
			self.db_connection = sqlite3.connect(self._db_dir)
			self.database_is_open = True
			return


	def _open_cursor(self):
		if self.cursor_is_open == False:
			self.cursor_is_open = True
			self.db_cursor = self.db_connection.cursor()
			return


	def _close_database(self):
		if self.database_is_open == True:
			self.database_is_open = False
			return


	def _close_cursor(self):
		if self.cursor_is_open == True:
			self.db_cursor.close()
			self.cursor_is_open = False
			return


class SqliteDatabaseTool(SqliteBase):


	def __init__(self, db_dir):
		super().__init__(db_dir)


	def exec(self, command_format):
		self._open_connection()
		exec_ = self.db_cursor.execute(command_format)
		self._close_connection()
		return


	def exec_commit(self, command_format):
		self._open_connection()
		exec_commit_ = self.db_cursor.execute(command_format)
		self.db_connection.commit()
		self._close_connection()
		return


	def exec_fetchone(self, command_format):
		self._open_connection()
		exec_fetchone_ = self.db_cursor.execute(command_format).fetchone()
		self._close_connection()
		return exec_fetchone_


	def exec_fetchmany(self, command_format):
		self._open_connection()
		exec_fetchmany_ = self.db_cursor.execute(command_format).fetchmany()
		self.close_connection()
		return exec_fetchmany_


	def exec_fetchall(self, command_format):
		self._open_connection()
		exec_fetchall_ = self.db_cursor.execute(command_format).fetchall()
		self._close_connection()
		return exec_fetchall_

