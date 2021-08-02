import discord
import sys, os
sys.path.append(os.path.abspath("."))
from dotenv import load_dotenv
from discord.ext import commands
from webserver import keep_alive
load_dotenv()


BOT_TOKEN = os.environ.get("BOT_TOKEN")


bot = commands.Bot(command_prefix='r/')

bot.load_extension("cogs.basic")

if __name__ == "__main__":
	keep_alive()
	bot.run(BOT_TOKEN)