from dataclasses import dataclass
import discord


@dataclass
class SetFields:
  user: str = ""
  title: str = "Setting {action} Position and Effect"
  description: str = "Custom built for {user}"
  footer: str = "To search for XP use \"mentions:{user} desperate\""
  reminder: str = "{user}, don't forget to mark XP for that desperate {action} roll."
  position: str = ""
  effect: str = ""
  action: str = ""

  positions = {
    "c": "**Controlled:** You act on your terms. You exploit a major advantage.",
    "r": "**Risky:** You go head-to-head. You act under fire. You take a chance.",
    "d": "**Desperate:** You overreach your capabilities. You’re in serious (but awesome) trouble. _Don't forget to mark experiece!_"
  }
  effects = {
    "l": "**Limited:** You achieve a partial or weak effect.",
    "s": "**Standard:** You achieve what we would expect as _normal_ with the action.",
    "g": "**Great:** You achieve more than usual."
  }
  actions = ["attune", "command", "consort", "doctor", "hack", "helm", "rig", "scramble", "scrap", "skulk", "study", "sway"]

  def __init__(self, args):
    print( args) 
    for value in args:
      if str(value).lower() in self.actions:
        self.action = value.capitalize()
      elif value.startswith("<@"):
        print ("got the user", value)
        self.user = value
      elif str(value)[0] in self.positions.keys():
        self.position = self.positions[str(value)[0]]
      elif str(value)[0] in self.effects.keys():
        self.effect = self.effects[str(value)[0]]
    
    if self.position == "":
      self.__init__(["r"])
    if self.effect == "":
      self.__init__(["s"])

class SetRoll():
  fields = None

  def __init__(self, args):
    self.fields = SetFields(args)

  def fillStr(self, value):
    value = value.replace("{user}", self.fields.user)
    value = value.replace("{action}", self.fields.action)

    return value

  def getEmbed(self):
    embed = discord.Embed(title=self.fillStr(self.fields.title), description = self.fillStr(self.fields.description))
    
    embed.add_field(name="_**Position:**_", value=self.fields.position, inline=True)
    embed.add_field(name="_**Effect:**_", value=self.fields.effect, inline=True)
    if self.fields.position.find( "Desperate" ) != -1:
      embed.set_footer(text = self.fillStr(self.fields.footer))
    
    return embed

