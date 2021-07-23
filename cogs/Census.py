import discord
from discord.ext import commands

class BotData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="showcache")
    async def getcashe(self, ctx):
        for msg in self.bot.cached_messages:
            print(msg.content)

def setup(bot):
    bot.add_cog(BotData(bot))