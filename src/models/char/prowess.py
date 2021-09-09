from src.models.char.from_raw import FromRaw

class ProwessModel(FromRaw):
  def __init__(self, xp=0,helm=0,scramble=0,scrap=0,skulk=0):
    self.xp = xp
    self.helm = helm
    self.scramble = scramble
    self.scrap = scrap
    self.skulk = skulk
    
  def to_dict(self):
    return {
      "xp": self.xp,
      "helm": self.helm,
      "scramble": self.scramble,
      "scrap": self.scrap,
      "skulk": self.skulk
    }

  def from_dict(self, source: dict):
    self.xp = source["xp"]
    self.helm = source["helm"]
    self.scramble = source["scramble"]
    self.scrap = source["scrap"]
    self.skulk = source["skulk"]

    return self

  def from_raw( self, source: dict):
    """
    Pulling in values from the data source
    prowess_xp1",prowess_xp2","prowess_xp3",prowess_xp4","prowess_xp5","prowess_xp6","helm1","helm2","helm3","helm4","scramble1","scramble2","scramble3","scramble4","scrap1","scrap2","scrap3","scrap4","sulk1","skulk2","skulk3","skulk4"
    """
     
    self.xp = self.get_total(source, 6, "prowess_xp")
    self.helm = self.get_total(source, 4, "helm")
    self.scramble = self.get_total(source, 4, "scramble")
    self.scrap = self.get_total(source, 4, "scrap")
    self.skulk = self.get_total(source, 4, "skulk")

    return self

  def __str__(self):
    return f"""**Prowess XP:** {self.num_to_dots(self.xp, 6)}
    **Helm:** {self.num_to_arrows(self.helm)}
    **Scramble:** {self.num_to_arrows(self.scramble)}
    **Scrap:** {self.num_to_arrows(self.scrap)}
    **Skulk:** {self.num_to_arrows(self.skulk)}""" 
    