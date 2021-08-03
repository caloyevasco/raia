from main import db_tool


class MemberCommands(Test):


	def __init__(self, text_channel_name):
		self.text_channel_name = text_channel_name


	def take(self, context):
		if context.channel.name = self.text_channel_name:
			return True
		else:
			return False


class PlayerCommands(MemberCommands):


	def __init__(self, text_channel_name):
		super().__init__(text_channel_name)


	def new_player(self, context):
		if self.take(context):
			if db_tool.create(context):
				return False
			else:
				return True