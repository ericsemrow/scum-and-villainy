import d20
import discord
class Action(object):
  num_die = None
  description = None
  title = None
  roll_result = {
    1: "Bad outcome",
    2: "Bad outcome",
    3: "Bad outcome",
    4: "Success with complications",
    5: "Success with complications",
    6: "Success",
    7: "Crit!"
  }

  def __init__(self, num_die: int):
    self.num_die = num_die
  

  def roll(self):
    if( self.num_die ):
      result = d20.roll( f"{self.num_die}d6kh1" )
    else:
      result = d20.roll( "2d6kl1" )

    return result
  
  def getRoll(self):
    result = self.roll()
    msg = self.roll_result[result.total]
    # if 6 check for crit
    if( result.total == 6 ):
      sixes = self.getNumSixes(result)
      if( sixes > 1):
        msg = self.roll_result[7]
    
    return f"{str(result)}: {msg}"
        

  def getNumSixes(self, result):
    return [int(die.values[0]) for die in result.expr.children[0].values].count(6)

  def getTitle(self, ctx):
    title = self.title.replace("{#}", str(self.num_die))
    title = title.replace("{name}", str(ctx.message.author.nick))
    return title

  def getEmbed(self, ctx):
    embed = discord.Embed(title=self.getTitle(ctx), description=self.description)
    embed.add_field(name=f"shake shake shake...roll.....", value=self.getRoll(), inline=True)
    
    return embed
