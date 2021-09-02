from src.actions.attune import Attune
from src.actions.command import Command
from src.actions.consort import Consort
from src.actions.doctor import Doctor
from src.actions.hack import Hack
from src.actions.helm import Helm
from src.actions.rig import Rig
from src.actions.scramble import Scramble
from src.actions.scrap import Scrap
from src.actions.skulk import Skulk
from src.actions.study import Study
from src.actions.sway import Sway

def start_actions(bot):
  # Actions
  @bot.command()
  async def attune(ctx, *args: int):
    die = args[0] if len(args) else 0
    await ctx.message.delete()
    await ctx.send(embed=Attune(die).getEmbed(ctx))

  @bot.command()
  async def command(ctx, *args: int):
    die = args[0] if len(args) else 0
    await ctx.message.delete()
    await ctx.send(embed=Command(die).getEmbed(ctx))

  @bot.command()
  async def consort(ctx, *args: int):
    die = args[0] if len(args) else 0
    await ctx.message.delete()
    await ctx.send(embed=Consort(die).getEmbed(ctx))

  @bot.command()
  async def doctor(ctx, *args: int):
    die = args[0] if len(args) else 0
    await ctx.message.delete()
    await ctx.send(embed=Doctor(die).getEmbed(ctx))

  @bot.command()
  async def hack(ctx, *args: int):
    die = args[0] if len(args) else 0
    await ctx.message.delete()
    await ctx.send(embed=Hack(die).getEmbed(ctx))

  @bot.command()
  async def helm(ctx, *args: int):
    die = args[0] if len(args) else 0
    await ctx.message.delete()
    await ctx.send(embed=Helm(die).getEmbed(ctx))

  @bot.command()
  async def rig(ctx, *args: int):
    die = args[0] if len(args) else 0
    await ctx.message.delete()
    await ctx.send(embed=Rig(die).getEmbed(ctx))

  @bot.command()
  async def scramble(ctx, *args: int):
    die = args[0] if len(args) else 0
    await ctx.message.delete()
    await ctx.send(embed=Scramble(die).getEmbed(ctx))

  @bot.command()
  async def scrap(ctx, *args: int):
    die = args[0] if len(args) else 0
    await ctx.message.delete()
    await ctx.send(embed=Scrap(die).getEmbed(ctx))

  @bot.command()
  async def skulk(ctx, *args: int):
    die = args[0] if len(args) else 0
    await ctx.message.delete()
    await ctx.send(embed=Skulk(die).getEmbed(ctx))

  @bot.command()
  async def study(ctx, *args: int):
    die = args[0] if len(args) else 0
    await ctx.message.delete()
    await ctx.send(embed=Study(die).getEmbed(ctx))

  @bot.command()
  async def sway(ctx, *args: int):
    die = args[0] if len(args) else 0
    await ctx.message.delete()
    await ctx.send(embed=Sway(die).getEmbed(ctx))
  