import d20
import discord

class UsesDice(object):
  title = None
  description = None
  num_die = None

 
  def roll(self):
    if( self.num_die ):
      result = d20.roll( f"{self.num_die}d6kh1" )
    else:
      result = d20.roll( "2d6kl1" )

    return result

  def getNumSixes(self, result):
    return [int(die.values[0]) for die in result.expr.children[0].values].count(6)

  def getTitle(self, ctx):
    name = str(ctx.message.author.nick if ctx.message.author.nick else ctx.message.author).split("#")[0]
    command = ctx.command.name.capitalize()

    title = self.title.replace("{#}", str(self.num_die))
    title = title.replace("{name}", name)
    title = title.replace("{action}", command)

    return title

  def getEmbed(self, ctx):
    embed = discord.Embed(title=self.getTitle(ctx), description=self.description)
    embed.add_field(name=f"shake shake shake...Boom.....", value=self.getRoll(), inline=True)
    
    return embed