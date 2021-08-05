import discord
import os
from databasetool.databasetool import DatabaseTool
from base import gamecommands
from dotenv import load_dotenv
from discord.ext import commands
from webserver.webserver import keep_alive
load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")


text_channel = "raia-main"


bot = commands.Bot(command_prefix='r/')

player_commands = gamecommands.PlayerCommands(text_channel)

bot.load_extension("cogs.basic")


def run():
	keep_alive()
	bot.run(BOT_TOKEN)