import os
import keepalive
import d20
from src.start_actions import start_actions
from src.start_resistances import start_resistances
from src.set import SetRoll

#from replit import db
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
print( "Starting" )

@bot.listen('on_ready')
async def is_ready():
    print("Online")

start_actions(bot)
start_resistances(bot)



@bot.command()
async def roll(ctx, *, arg):
  await ctx.send(str(d20.roll(arg)))
  
@bot.command()
async def r(ctx, *, arg):
  await ctx.send(str(d20.roll(arg)))

@bot.command()
async def set(ctx, *args):
  await ctx.message.delete()
  await ctx.send(embed=SetRoll(args).getEmbed())

keepalive.keep_alive()
token = os.environ.get("DISCORD_TOKEN") 
bot.run(token)