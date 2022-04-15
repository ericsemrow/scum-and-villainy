import os, json
from discord.ext import commands
from src.repositories.character_repository import CharacterRepository
from src.uses_dice import UsesDice
 
class Resistances(UsesDice, commands.Cog):

  title = "{name} is resisting with {#} {action} die"
  roll_result = {
    1: "Ouch. Mark 5 stress.",
    2: "Mark 4 stress.",
    3: "Mark 3 stress.",
    4: "Mark 2 stress.",
    5: "Mark 1 stress.",
    6: "No stress at all.",
    7: "Crit! Clear one stress."
  }

  def __init__(self, bot):
    super().__init__()
    
    filepath = os.path.join(os.path.relpath("src/gamedata"), "resistances.json")
    f = open(filepath, "r")
    self.resistance_data = json.load(f)
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
    self.num_die = args[0] if len(args) else self.attrRatingFromSheet(ctx, ctx.command.name.lower())
    self.description = self.resistance_data[ctx.command.name.lower()]["desc"]

    try:
      await ctx.message.delete()
    except Exception as e:
      await ctx.send( str(e) )

    await ctx.send(embed=self.getEmbed(ctx))

  def attrRatingFromSheet(self, ctx, attr):
    charRepo = CharacterRepository()
    char = charRepo.get_active_character_for_user(ctx.author.id)
    if char:
      attribute = getattr(char, attr)
      return attribute.getRating()
    else:
      return 0

      
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def insight(self, ctx, *args: int):
    """!insight <num of dice to roll (defaults to sheet value)>"""
    await self.executeAction(args, ctx)
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def prowess(self, ctx, *args: int):
    """!prowess <num of dice to roll (defaults to sheet value)>"""
    await self.executeAction(args, ctx)
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def resolve(self, ctx, *args: int):
    """!resolve <num of dice to roll (defaults to sheet value)>"""
    await self.executeAction(args, ctx)
  
  @insight.error
  @prowess.error
  @resolve.error
  async def handle_bot_exceptions(self, ctx, error):
    bugsnag.notify(error)
    await ctx.send( str(error) )
