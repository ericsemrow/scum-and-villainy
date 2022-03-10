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


  async def confirm(self, ctx, msg):
    channel = ctx.message.channel
    def check(m):
      return (m.content.lower == 'yes' or 'no') and m.channel == channel
  
    await ctx.send(f"{msg} Do you wish to continue? (yes/no)")
    msg = await ctx.bot.wait_for("message", check=check, timeout=30)
    
    if msg.content.lower() == "yes":
      return True
    else:
      return False
      
  async def determine_which(self, ctx, options):
    if not len(options):
      # can't find anything close
      await ctx.send("No matching options")

      return
    elif len(options) > 1:
      # well now we have too many options
      query_msg = """More than one option matches your request.

      reply"""
      for i in range(len(options)):
        query_msg += f"""
        {i+1}: {options[i]}"""

      channel = ctx.message.channel
      def check(m):
        return m.content.isnumeric and m.channel == channel

      await ctx.send(query_msg)
      msg = await ctx.bot.wait_for("message", check=check, timeout=30)
      
      name = int(msg.content) - 1
    else:
      name = 0
      
    return name