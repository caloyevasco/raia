import discord
import sys, os
sys.path.append(os.path.abspath("."))
from dotenv import load_dotenv
from discord.ext import commands
from webserver.webserver import keep_alive
import run
load_dotenv()


run.market_system.create_table(run.market_table)
run.player_system.create_table(run.player_table)


BOT_TOKEN = os.environ.get("BOT_TOKEN")


bot = commands.Bot(command_prefix='r/')

bot.load_extension('market_database_tool.marketcog')
bot.load_extension('player_database_tool.playercog')

if __name__ == "__main__":
	keep_alive()
	bot.run(BOT_TOKEN)