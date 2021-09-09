from src.models.char.from_raw import FromRaw

class InsightModel(FromRaw):
  def __init__(self, xp=0,doctor=0,hack=0,rig=0,study=0):
    self.xp = xp
    self.doctor = doctor
    self.hack = hack
    self.rig = rig
    self.study = study
    
  def to_dict(self):
    return {
      "xp": self.xp,
      "doctor": self.doctor,
      "hack": self.hack,
      "rig": self.rig,
      "study": self.study
    }

  def from_dict(self, source: dict):
    self.xp = source["xp"]
    self.doctor = source["doctor"]
    self.hack = source["hack"]
    self.rig = source["rig"]
    self.study = source["study"]

    return self


  def from_raw(self, source: dict):
    """
    "AW9":"insight_xp1","AX9":"insight_xp2","AY9":"insight_xp3","AZ9":"insight_xp4","BB9":"insight_xp5","BA9":"insight_xp6","doctor1","doctor2","doctor3","doctor4","hack1","hack2","hack3","hack4","rig1","rig2","rig3","rig4","study1","study2","study3"

    """
    
    self.xp = self.get_total(source, 6, "insight_xp")
    self.doctor = self.get_total(source, 4, "doctor")
    self.hack = self.get_total(source, 4, "hack")
    self.rig = self.get_total(source, 4, "rig")
    self.study = self.get_total(source, 4, "study")

    return self

  
  def __str__(self):
    return f"""**Insight XP:** {self.num_to_dots(self.xp, 6)}
    **Doctor:** {self.num_to_arrows(self.doctor)}
    **Hack:** {self.num_to_arrows(self.hack)}
    **Rig:** {self.num_to_arrows(self.rig)}
    **Study:** {self.num_to_arrows(self.study)}""" 
    