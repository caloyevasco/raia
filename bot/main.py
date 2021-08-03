import discord
import os
from databasetool.databasetool import DatabaseTool
from base.gamecommands import MemberCommands
from dotenv import load_dotenv
from discord.ext import commands
from webserver.webserver import keep_alive
load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")


text_channel = "raia-main"
db_tool = DatabaseTool('database.json')


bot = commands.Bot(command_prefix='r/')


member_commands = MemberCommands(text_channel)
player_commands = PlayerCommands(text_channel)

bot.load_extension("cogs.bot-raia")
bot.load_extension("cogs.basic")


def run():
	keep_alive()
	bot.run(BOT_TOKEN)