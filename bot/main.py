import discord
import os
from base.gamecommands import MemberCommands
from dotenv import load_dotenv
from discord.ext import commands
from webserver.webserver import keep_alive
load_dotenv()

text_channel = "raia-main"

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = commands.Bot(command_prefix='r/')

process_commands = MemberCommands(bot, text_channel)

bot.load_extension("cogs.bot-raia")
bot.load_extension("cogs.basic")


def run():
	keep_alive()
	bot.run(BOT_TOKEN)