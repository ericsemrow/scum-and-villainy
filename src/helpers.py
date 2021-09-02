from discord.ext import commands
import d20
from src.set import SetRoll

class Helpers(commands.Cog):

  @commands.command(aliases=['r'])
  async def roll(self, ctx, *, arg):
    """Standard dice roller. Alias: r"""
    await ctx.send(str(d20.roll(arg)))

  @commands.command()
  async def set(self, ctx, *args):
    """
      Receives up to four arguments: User Ping, Position, Effect, Action

      These can be sent in any order. In addition Position and Effect only require the first character to match. E.g. Risky can be sent as risky, r, ramalamadingdong, or ris. If nothing matches position or effect they will be set to the default of Risky/Standard

      Ex. !set sway d s @CoolGuy123
      Ex. !set @CoolGuy321 sway
    """
    await ctx.message.delete()
    await ctx.send(embed=SetRoll(args).getEmbed())
