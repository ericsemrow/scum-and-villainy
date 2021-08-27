from src.resistances.insight import Insight
from src.resistances.prowess import Prowess
from src.resistances.resolve import Resolve

def start_resistances(bot):
  # Resistances
  @bot.command()
  async def insight(ctx, *args: int):
    die = args[0] if len(args) else 0
    await ctx.send(embed=Insight(die).getEmbed(ctx))

  @bot.command()
  async def prowess(ctx, *args: int):
    die = args[0] if len(args) else 0
    await ctx.send(embed=Prowess(die).getEmbed(ctx))

  @bot.command()
  async def resolve(ctx, *args: int):
    die = args[0] if len(args) else 0
    await ctx.send(embed=Resolve(die).getEmbed(ctx))
