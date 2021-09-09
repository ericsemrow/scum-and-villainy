from src.models.char.from_raw import FromRaw

class ResolveModel(FromRaw):
  def __init__(self, xp=0,attune=0,command=0,consort=0,sway=0):
    self.xp = xp
    self.attune = attune
    self.command = command
    self.consort = consort
    self.sway = sway
    
  def to_dict(self):
    return {
      "xp": self.xp,
      "attune": self.attune,
      "command": self.command,
      "consort": self.consort,
      "sway": self.sway
    }

  def from_dict(self, dict):
    self.xp = dict["xp"]
    self.attune = dict["attune"]
    self.command = dict["command"]
    self.consort = dict["consort"]
    self.sway = dict["sway"]

    return self

  def from_raw(self, source: dict):
    """
    "resolve_xp1","resolve_xp2","resolve_xp3","resolve_xp4","resolve_xp5","resolve_xp6","attune1","attune2","attune3","attune4","command1","command2","command3","command4","consort1","consort2","consort3","consort4","sway1","sway2","sway3","sway4"

    """
    
    self.xp = self.get_total(source, 6, "resolve_xp")
    self.attune = self.get_total(source, 4, "attune")
    self.command = self.get_total(source, 4, "command")
    self.consort = self.get_total(source, 4, "consort")
    self.sway = self.get_total(source, 4, "sway")

    return self

  def __str__(self):
    return f"""**Resolve XP:** {self.num_to_dots(self.xp, 6)}
    **Attune:** {self.num_to_arrows(self.attune)}
    **Command:** {self.num_to_arrows(self.command)}
    **Consort:** {self.num_to_arrows(self.consort)}
    **Sway:** {self.num_to_arrows(self.sway)}""" 