from src.models.char.from_raw import FromRaw

class ArmorModel(FromRaw):
  def __init__(self,armor=0,heavy=0,special=0):
    self.armor = armor
    self.heavy = heavy
    self.special = special
  
  def to_dict(self):
    return {
      "armor": self.armor,
      "heavy": self.heavy,
      "special": self.special
    }
  
  def from_dict(self, source: dict):
    self.armor = bool(source["armor"])
    self.heavy = bool(source["heavy"])
    self.special = bool(source["special"])

    return self

  def from_raw(self, source: dict):
    """
    "armor","heavy","special"
    """
    self.from_dict(source)

    return self
  
  def __str__(self):
    return f"""**Armor:** {self.bool_to_dot(self.armor)}
    **Heavy:** {self.bool_to_dot(self.heavy)}
    **Special:** {self.bool_to_dot(self.special)}"""