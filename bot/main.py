import discord
from dotenv import load_dotenv
from discord.ext import commands
from webserver import keep_alive
load_dotenv()


BOT_TOKEN = os.environ.get("BOT_TOKEN")


bot = commands.Bot(command_prefix='r/')

bot.load_extension("cogs.basic")

def run():
	keep_alive()
	bot.run(BOT_TOKEN)