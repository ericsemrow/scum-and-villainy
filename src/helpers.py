import discord
from discord.ext import commands
import d20
from src.set import SetRoll
import argparse


parser = argparse.ArgumentParser(description='Take in params')
parser.add_argument('-i', "--image", type=str, help='An image URL')
parser.add_argument('-d', "--description", type=str, help='The description text')
parser.add_argument('-n', "--name", type=str, help='The character name')

class Helpers(commands.Cog):
  @commands.command(aliases=['r'])
  @commands.has_permissions(send_messages=True)
  async def roll(self, ctx, arg):
    """Standard dice roller. Alias: r"""
    await ctx.send(str(d20.roll(arg)))

  @commands.command(aliases=['e'])
  @commands.has_permissions(send_messages=True)
  async def npc(self, ctx, *args):
    """A helper function to print info about an npc
    -i = image url
    -n = name
    -d = description"""
    parsed = parser.parse_args(args)
    embed = discord.Embed(title=parsed.name,description=parsed.description)
    if parsed.image is not None:
      embed.set_thumbnail( url=parsed.image )

    await ctx.message.delete()
    await ctx.send(embed=embed)

  @commands.command()  
  @commands.has_permissions(manage_messages=True)
  async def set(self, ctx, *args):
    """
      Receives up to four arguments: User Ping, Position, Effect, Action

      These can be sent in any order. In addition Position and Effect only require the first character to match. E.g. Risky can be sent as risky, r, ramalamadingdong, or ris. If nothing matches position or effect they will be set to the default of Risky/Standard

      Ex. !set sway d s @CoolGuy123
      Ex. !set @CoolGuy321 sway
    """
    await ctx.message.delete()
    await ctx.send(embed=SetRoll(args).getEmbed())

  @roll.error
  @set.error
  async def handle_bot_exceptions(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send("This bot seems to be missing the required permissions.")
    if isinstance(error, commands.CommandInvokeError):
      await ctx.send("This bot seems to be missing the required permission.")