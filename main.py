import os
import keepalive
from src.actions import Actions
from src.resistances import Resistances
from src.helpers import Helpers
from src.char_tools import CharTools

#from replit import db
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.listen('on_ready')
async def is_ready():
    print("Online")

bot.add_cog(Actions(bot))
bot.add_cog(Resistances(bot))
bot.add_cog(Helpers(bot))
bot.add_cog(CharTools(bot))


keepalive.keep_alive()
token = os.environ.get("DISCORD_TOKEN") 
bot.run(token)