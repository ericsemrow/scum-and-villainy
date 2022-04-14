import os
import bugsnag
from src.actions import Actions
from src.resistances import Resistances
from src.helpers import Helpers
from src.char_tools import CharTools

from discord.ext import commands

bugsnag.configure(
    api_key="8b60d1890a58f9fcc3dc8627809a361a",
    project_root="/opt/scum-and-villainy/",
)

import logging

from bugsnag.handlers import BugsnagHandler

# ... (call bugsnag.configure() here)
logger = logging.getLogger("scum")
handler = BugsnagHandler()
# send only ERROR-level logs and above
handler.setLevel(logging.ERROR)
logger.addHandler(handler)


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
