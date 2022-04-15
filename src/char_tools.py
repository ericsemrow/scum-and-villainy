import discord
from discord.ext import commands
from src.repositories.google_sheets import GoogleSheets
from src.repositories.character_repository import CharacterRepository
from src.uses_dice import UsesDice

class CharTools(commands.Cog, UsesDice):
  
  @commands.command()
  async def gsheet(self, ctx, arg):
    """!gsheet <link to google sheet>
    Make a **copy** of this sheet and drag your playbook tab to the left-most position: https://docs.google.com/spreadsheets/d/1SBI4wjgHUPNGEqmFlR3gY3SEzPh7e8sCA14ilQlXP-g/edit?usp=sharing"""

    if await self.confirm(ctx, "Is your playbook the left-most sheet?"):
      g_sheets = GoogleSheets()
      char_repo = CharacterRepository()
      sheet_id = g_sheets.get_sheet_id(arg)
      sheet_data = g_sheets.get_sheet_by_id(sheet_id)
      char = char_repo.get_char_from_raw(sheet_data)
      char_repo.store_character_for_user(char, ctx.author.id)
  
      await ctx.send("Sheet successfully imported! Use `!sheet` to print.")
    

  @commands.command()
  async def update(self, ctx):
    """Updates the currently active google sheet"""
    
        
    if await self.confirm(ctx, "This action will overwrite your bot character including stress and xp."):
      char_repo = CharacterRepository()
    
      char = char_repo.get_active_character_for_user(ctx.author.id)
      print(char)
      await self.gsheet(ctx, f'/spreadsheets/d/{char.sheet_id}')
    
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def sheet(self, ctx):
    """!sheet
    Print out a friendly copy of your active character sheet."""
    char_repo = CharacterRepository()
    char = char_repo.get_active_character_for_user(ctx.author.id)

    if char is not None:
      await ctx.message.delete()
      await ctx.send(embed=char_repo.getEmbed(ctx, char))
    else:
      await self.handle_no_sheet(ctx)
    
  @commands.command()
  @commands.has_permissions(send_messages=True)
  async def xp(self, ctx, type="pl", amount=0):
    """Add or remove xp for either your playbook or an attribute.
    Ex: !xp 2 (adds 2 xp to your playbook)
    Ex: !xp insight 1 (adds 1 xp to insight)"""

    char_repo = CharacterRepository()
    char = char_repo.get_active_character_for_user(ctx.author.id)
    if char is not None:
      report = char_repo.add_xp(ctx.author.id, char, type, int(amount))
      await ctx.message.delete()
      await ctx.send(embed=discord.Embed(description=str(report)))
    else:
      await self.handle_no_sheet(ctx)

  @commands.command()
  @commands.has_permissions(send_messages=True)
  async def stress(self, ctx, amount=0):
    """Add or remove stress from your character sheet
    Ex: !stress 2 (adds 2 stress)
    Ex: !stress -1 (removes 1 stress)"""
    
    char_repo = CharacterRepository()
    char = char_repo.get_active_character_for_user(ctx.author.id)
    if char is not None:
      report = char_repo.add_stress(ctx.author.id, char, int(amount))
      await ctx.message.delete()
      await ctx.send(embed=discord.Embed(description=str(report)))
    else:
      await self.handle_no_sheet(ctx)
    
  @commands.command()
  async def char(self, ctx, *, arg):
    """Change active characters by name or alias
    Ex: !char Romeo
    Ex: !char Hot Shot"""
    print(arg)
    char_repo = CharacterRepository()
    char = await char_repo.get_character_by_title(ctx, ctx.author.id, arg)

    char_repo.switch_active_character(ctx.author.id, char)
    await ctx.send(f"Active Character: {char.name} ({char.alias})")
    
  async def handle_no_sheet(self, ctx):
    await ctx.send("No sheet loaded. Have you used `!sheet <url>`?")

  @sheet.error
  @update.error
  @gsheet.error
  @char.error
  @stress.error
  @xp.error
  async def handle_bot_exceptions(self, ctx, error):
      bugsnag.notify(error)
      await ctx.send( str(error) )