import discord
import os
import keepalive
import d20
from src.start_actions import start_actions

#from replit import db
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
print( "Starting" )

@bot.listen('on_ready')
async def is_ready():
    print("Online")

start_actions(bot)



@bot.command()
async def roll(ctx, *, arg):
  await ctx.send(str(d20.roll(arg)))
@bot.command()
async def r(ctx, *, arg):
  await ctx.send(str(d20.roll(arg)))

keepalive.keep_alive()
token = os.environ.get("DISCORD_TOKEN") 
bot.run(token)