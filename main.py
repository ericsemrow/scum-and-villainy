import os
from src.actions import Actions
from src.resistances import Resistances
from src.helpers import Helpers
from src.char_tools import CharTools

from discord.ext import commands
from src.log import Log

logger = Log()

bot = commands.Bot(command_prefix='!')

@bot.listen('on_ready')
async def is_ready():
    print("Online")


bot.add_cog(Actions(bot))
bot.add_cog(Resistances(bot))
bot.add_cog(Helpers(bot))
bot.add_cog(CharTools(bot))


token = os.environ.get("DISCORD_TOKEN") 
bot.run(token)
