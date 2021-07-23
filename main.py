import os, sys
import discord
from discord.ext import commands
from webserver.webserver import keep_alive
from dotenv import load_dotenv
sys.path.append(os.path.abspath("."))

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = commands.Bot(command_prefix='r/')

bot.load_extension("cogs.Wake")
bot.load_extension("cogs.Moneys")
bot.load_extension("cogs.Census")

if __name__ == "__main__":
	keep_alive()
	bot.run(BOT_TOKEN)