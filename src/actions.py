import os, json
from discord.ext import commands
from src.uses_dice import UsesDice
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
        
  async def executeAction(self, args, ctx):
    self.num_die = args[0] if len(args) else 0
    self.description = self.action_data[ctx.command.name.lower()]["desc"]

    await ctx.message.delete()
    await ctx.send(embed=self.getEmbed(ctx))

  @commands.command()
  async def attune(self, ctx, *args: int):
    """!attune <num of dice to roll (defaults to 0)>"""
    await self.executeAction(args, ctx)
  
  @commands.command()
  async def command(self, ctx, *args: int):
    """!command <num of dice to roll (defaults to 0)>"""
    await self.executeAction(args, ctx)

  @commands.command()
  async def consort(self, ctx, *args: int):
    """!consort <num of dice to roll (defaults to 0)>"""
    await self.executeAction(args, ctx)
  
  @commands.command()
  async def doctor(self, ctx, *args: int):
    """!doctor <num of dice to roll (defaults to 0)>"""
    await self.executeAction(args, ctx)
  
  @commands.command()
  async def hack(self, ctx, *args: int):
    """!hack <num of dice to roll (defaults to 0)>"""
    await self.executeAction(args, ctx)
  
  @commands.command()
  async def helm(self, ctx, *args: int):
    """!helm <num of dice to roll (defaults to 0)>"""
    await self.executeAction(args, ctx)

  @commands.command()
  async def rig(self, ctx, *args: int):
    """!rig <num of dice to roll (defaults to 0)>"""
    await self.executeAction(args, ctx)
  
  @commands.command()
  async def scramble(self, ctx, *args: int):
    """!scramble <num of dice to roll (defaults to 0)>"""
    await self.executeAction(args, ctx)
  
  @commands.command()
  async def scrap(self, ctx, *args: int):
    """!scrap <num of dice to roll (defaults to 0)>"""
    await self.executeAction(args, ctx)
  
  @commands.command()
  async def skulk(self, ctx, *args: int):
    """!skulk <num of dice to roll (defaults to 0)>"""
    await self.executeAction(args, ctx)
  
  @commands.command()
  async def study(self, ctx, *args: int):
    """!study <num of dice to roll (defaults to 0)>"""
    await self.executeAction(args, ctx)
  
  @commands.command()
  async def sway(self, ctx, *args: int):
    """!sway <num of dice to roll (defaults to 0)>"""
    await self.executeAction(args, ctx)