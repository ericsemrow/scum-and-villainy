import discord, re
from src.models.firestore import Firestore
from src.models.char.character import Character
from src.repositories.user_repository import UserRepository
from src.uses_dice import UsesDice

class CharacterRepository(Firestore,UsesDice):

  COL = "characters"
  
  def get_active_character_for_user(self, user_id):
    user_repo = UserRepository()
    user = user_repo.get_user_or_create( user_id )
    active_char = user.active_character
    doc = user_repo.get_user_ref( user_id ).collection(self.COL).document(active_char).get()
    if doc.exists:
      return Character().from_dict(doc.to_dict())

  async def get_character_by_title(self, ctx, user_id, title):
    user_repo = UserRepository()
    docs = user_repo.get_user_ref( user_id ).collection(self.COL).stream()
    names = []
    chars = []
    for doc in docs:
      char = Character().from_dict(doc.to_dict())
      if (title.lower() in char.name.lower()) or (title in char.alias.lower()):
        chars.append(char)
        names.append(f'Name: {char.name} Alias: {char.alias}')

    index = await self.determine_which(ctx, names)
    
    if index is not None:
      char = chars[index]
      return char
    
    
    
  def store_character_for_user(self, char: Character, user_id):
    user_repo = UserRepository()
    user = user_repo.get_user_or_create( user_id )
    user_repo.get_user_ref( user_id ).collection(self.COL).document(char.id).set(char.to_dict())
    user.active_character = char.id
    user_repo.store_user(user)
    

  def switch_active_character(self, user_id, char: Character):
    user_repo = UserRepository()
    user_repo.get_user_ref( user_id ).set({"data": {"active_character": char.id}}, merge=True)

  def get_char_from_raw(self, raw: dict):
    char = Character()
    char.from_raw(raw)
    
    return char

  def add_xp( self, user, char: Character, attr: str, amount: int):
    types = {
      "pl": "playbook_xp",
      "in": "insight",
      "pr": "prowess",
      "re": "resolve"
    }
    abbrev = attr[0:2]
    if abbrev == "pl":
      char.playbook_xp += amount
    else:
      try:
        attribute = getattr(char, types[abbrev])
        attribute.xp += amount
      except KeyError:
        return None
    
    self.store_character_for_user( char, user)
    
    return char.get_xp()

  def add_stress( self, user, char: Character, amount: int):
    
    char.stress += amount
    attribute = char.get_stress()
    
    self.store_character_for_user( char, user)
    
    return attribute

  def getSkills(self, ctx, char: Character):
    return {**char.insight.to_dict(), **char.prowess.to_dict(), **char.resolve.to_dict()}
  
  def getEmbed(self, ctx, char: Character):
    embed = discord.Embed(title=char.name, description=str(char))
    
    return embed