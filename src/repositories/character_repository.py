import discord
from src.models.firestore import Firestore
from src.models.char.character import Character
from src.repositories.user_repository import UserRepository

class CharacterRepository(Firestore):

  COL = "characters"
  
  def get_active_character_for_user(self, user_id):
    user_repo = UserRepository()
    user = user_repo.get_user_or_create( user_id )
    active_char = user.active_character
    doc = user_repo.get_user_ref( user_id ).collection(self.COL).document(active_char).get()
    if doc.exists:
      return Character().from_dict(doc.to_dict())
  
  def store_character_for_user(self, char: Character, user_id):
    user_repo = UserRepository()
    user = user_repo.get_user_or_create( user_id )
    user_repo.get_user_ref( user_id ).collection(self.COL).document(char.id).set(char.to_dict())
    user.active_character = char.id
    user_repo.store_user(user)
    

  def switch_active_character(self, name: str):
    pass

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
      attribute = char
    else:
      try:
        attribute = getattr(char, types[abbrev])
        attribute.xp += amount
      except KeyError:
        return None
    
    self.store_character_for_user( char, user)
    
    return attribute

  def getSkills(self, ctx, char: Character):
    return {**char.insight.to_dict(), **char.prowess.to_dict(), **char.resolve.to_dict()}
  
  def getEmbed(self, ctx, char: Character):
    embed = discord.Embed(title=char.name, description=str(char))
    
    return embed