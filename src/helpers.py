import discord, d20, argparse, os, json
from discord.ext import commands
from src.set import SetRoll


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

  @commands.command(aliases=['dm'])
  @commands.has_permissions(send_messages=True)
  async def botvoice(self, ctx, *, arg):
    """Make the bot say whatever you like. !dm Hey there."""
    await ctx.message.delete()
    await ctx.send(arg)


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


  @commands.command()  
  @commands.has_permissions(manage_messages=True)
  async def setup(self, ctx, arg):
    
    filepath = os.path.join(os.path.relpath("src/gamedata"), "server_template.json")
    f = open(filepath, "r")
    template = json.load(f)
    f.close()

    if arg == "channels":

      for group in template["groups"]:
        category = discord.utils.get(ctx.guild.categories, name=group["name"])
        if category is None:
          category = await ctx.guild.create_category(group["name"])
        for json_channel in group["channels"]:
          channel = discord.utils.get(ctx.guild.channels, name=json_channel["name"])
          if channel is None:
            channel = await ctx.guild.create_text_channel(json_channel["name"], category=category)
          
          for post in json_channel["posts"]:
            exists = False
            async for message in channel.history(limit=25):
              if message.content == post:
                exists = True
                break

            if not exists:
              post = await channel.send(content=post)
              
    if arg == "roles":
      for json_role in template["roles"]:
        role = discord.utils.get(ctx.guild.roles, name=json_role["name"])
        if role is None:
          color = getattr(discord.Colour, json_role["colour"])
          role = await ctx.guild.create_role(name=json_role["name"], colour=color(), mentionable=True)


  @roll.error
  @set.error
  @setup.error
  @botvoice.error
  @npc.error
  async def handle_bot_exceptions(self, ctx, error):
    bugsnag.notify(error)
    await ctx.send( str(error) )