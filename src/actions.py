import os, json, argparse, bugsnag
from discord.ext import commands
from src.uses_dice import UsesDice
from src.repositories.character_repository import CharacterRepository


parser = argparse.ArgumentParser(description='Take in params')
parser.add_argument('-b', "--bonus", default=0, type=int, help='Dice to add to your roll')


class Actions(UsesDice, commands.Cog):
  
  description = None
  roll_result = {
    1: "Bad outcome",
    2: "Bad outcome",
    3: "Bad outcome",
    4: "Success with complications",
    5: "Success with complications",
    6: "Success",
    7: "Crit!"
  }
  
  title = "{name} is rolling {#} {action} die"

  def __init__(self, bot):
    super().__init__()
    
    filepath = os.path.join(os.path.relpath("src/gamedata"), "actions.json")
    f = open(filepath, "r")
    self.action_data = json.load(f)
    f.close()


  def getRoll(self):
    result = self.roll()
    msg = self.roll_result[result.total]
    # if 6 check for crit
    if( result.total == 6 and self.num_die != 0 ):
      sixes = self.getNumSixes(result)
      if( sixes > 1):
        msg = self.roll_result[7]
    
    return f"{str(result)}: {msg}"
  
  async def executeAction(self, ctx, args):
    try:
      parsed = parser.parse_args(args)
    except:
      parsed = 0

    self.num_die = await self.skillFromSheet(ctx, ctx.command.name.lower())

    self.num_die += parsed.bonus

    self.description = self.action_data[ctx.command.name.lower()]["desc"]
    try:
      await ctx.message.delete()
    except Exception as e:
      await ctx.send( str(e) )

    await ctx.send(embed=self.getEmbed(ctx))

  async def skillFromSheet(self, ctx, skill):
    charRepo = CharacterRepository()
    char = charRepo.get_active_character_for_user(ctx.author.id)
    if char:
      points = charRepo.getSkills(ctx, char)
      return points[skill]
    else:
      return 0

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def attune(self, ctx, *args):
    """!attune - Rolls num of dice on active sheet"""
    await self.executeAction(ctx, args)
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def command(self, ctx, *args):
    """!command - Rolls num of dice on active sheet"""
    await self.executeAction(ctx, args)

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def consort(self, ctx, *args):
    """!consort - Rolls num of dice on active sheet"""
    await self.executeAction(ctx, args)
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def doctor(self, ctx, *args):
    """!doctor - Rolls num of dice on active sheet"""
    await self.executeAction(ctx, args)
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def hack(self, ctx, *args):
    """!hack - Rolls num of dice on active sheet"""
    await self.executeAction(ctx, args)
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def helm(self, ctx, *args):
    """!helm - Rolls num of dice on active sheet"""
    await self.executeAction(ctx, args)

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def rig(self, ctx, *args):
    """!rig - Rolls num of dice on active sheet"""
    await self.executeAction(ctx, args)
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def scramble(self, ctx, *args):
    """!scramble - Rolls num of dice on active sheet"""
    await self.executeAction(ctx, args)
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def scrap(self, ctx, *args):
    """!scrap - Rolls num of dice on active sheet"""
    await self.executeAction(ctx, args)
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def skulk(self, ctx, *args):
    """!skulk - Rolls num of dice on active sheet"""
    await self.executeAction(ctx, args )
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def study(self, ctx, *args):
    """!study - Rolls num of dice on active sheet"""
    await self.executeAction(ctx, args)
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def sway(self, ctx, *args):
    """!sway - Rolls num of dice on active sheet"""
    await self.executeAction(ctx, args)


  @attune.error
  @command.error
  @consort.error
  @doctor.error
  @hack.error
  @helm.error
  @rig.error
  @scramble.error
  @scrap.error
  @skulk.error
  @study.error
  @sway.error
  async def handle_bot_exceptions(self, ctx, error):
    bugsnag.notify(error)
    await ctx.send( str(error) )