class HarmModel():
  def __init__(self,level=1,desc=""):
    self.level = level
    self.desc = desc
  
  def to_dict(self):
    return {
      "level": self.level,
      "desc": self.desc
    }
  
  def from_dict(self, source: dict):
    self.level = source["level"]
    self.desc = source["desc"]