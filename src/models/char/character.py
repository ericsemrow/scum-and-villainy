from src.models.char.insight import InsightModel
from src.models.char.prowess import ProwessModel
from src.models.char.resolve import ResolveModel
from src.models.char.armor import ArmorModel
from src.models.char.from_raw import FromRaw

class Character(FromRaw):

  @property
  def insight(self):
    return self._insight

  @property
  def prowess(self):
    return self._prowess

  @property
  def resolve(self):
    return self._resolve

  @property
  def armor(self):
    return self._armor

  @property
  def trauma(self):
    return self._trauma

  @property
  def harm(self):
    return self._harm

  @property
  def healing(self):
    return self._healing

  @property
  def abilities(self):
    return self._abilities

  def __init__(self, id=None,playbook="",name="",crew="",alias="",look="",heritage="",background="",vice="",stress="",playbook_xp=0,insight=None,prowess=None,resolve=None,armor=None,trauma=None,harm=[],healing=[],abilities=[]):

    if insight is None:
      insight = InsightModel()
    if prowess is None:
      prowess = ProwessModel()
    if resolve is None:
      resolve = ResolveModel()
    if armor is None:
      armor = ArmorModel()
    if abilities is None:
      abilities

    self.id = id
    self.playbook = playbook
    self.name = name
    self.crew = crew
    self.alias = alias
    self.look = look
    self.heritage = heritage
    self.background = background
    self.vice = vice
    self.stress = stress
    self.playbook_xp = playbook_xp
    
    # These might need additional objects

    self._insight = insight
    self._prowess = prowess
    self._resolve = resolve
    self._armor = armor

    #not implemented yet
    self._trauma = trauma
    self._harm = harm
    self._healing = healing
    self._abilities = abilities

  @insight.setter
  def insight(self, val):
    if isinstance(val, InsightModel):
      self._insight = val
    elif isinstance(val, dict):
      self._insight = InsightModel().from_raw(val)

  @prowess.setter
  def prowess(self, val: ProwessModel):
    if isinstance(val, ProwessModel):
      self._prowess = val
    elif isinstance(val, dict):
      self._prowess = ProwessModel().from_raw(val)
    
  @resolve.setter
  def resolve(self, val: ResolveModel):
    if isinstance(val, ResolveModel):
      self._resolve = val
    elif isinstance(val, dict):
      self._resolve = ResolveModel().from_raw(val)

  @armor.setter
  def armor(self, val: ArmorModel):
    if isinstance(val, ArmorModel):
      self._armor = val
    elif isinstance(val, dict):
      self._armor = ArmorModel().from_raw(val)
    
  @trauma.setter
  def trauma(self, val: list):
    self._trauma = val
    
  @harm.setter
  def harm(self, val: list):
    self._harm = val
    
  @healing.setter
  def healing(self, val: list):
    self._healing = val
    
  @abilities.setter
  def abilities(self, val: list):
    self._abilities = val

  def from_dict(self, source: dict):
    self.set_basic_vars(source)
    self.id = source["id"]
    
    # These might need additional objects
    self._insight = InsightModel().from_dict(source["insight"])
    self._prowess = ProwessModel().from_dict(source["prowess"])
    self._resolve = ResolveModel().from_dict(source["resolve"])
    self._armor = ArmorModel().from_dict(source["armor"])
    self.stress = source["stress"]
    self._abilities = source["abilities"]
    self.playbook_xp = source["playbook_xp"]

    #Not implemented yet
    #self.trauma = source["trauma"]
    #self.harm = source["harm"]
    #self.healing = source["healing"]

    return self
    

  def to_dict(self):
    return {
      "id": self.id,
      "playbook": self.playbook,
      "name": self.name,
      "crew": self.crew,
      "alias": self.alias,
      "look": self.look,
      "heritage": self.heritage,
      "background": self.background,
      "vice": self.vice,
      "stress": self.stress,
      "playbook_xp": self.playbook_xp,
      # These might need additional objects
      "insight": self._insight.to_dict(),
      "prowess": self._prowess.to_dict(),
      "resolve": self._resolve.to_dict(),
      "armor": self._armor.to_dict(),
      #"trauma": self.trauma.to_dict(),
      #"harm": self.harm.to_dict(),
      #"healing": self.healing.to_dict(),
      "abilities": self._abilities
    }
  
  def from_raw(self, raw: dict):
    """
      {"id","playbook","name","crew","alias","look","heritage","heritage_override","background","background_override","vice","vice_override","stress_1","stress_2","stress_3","stress_4","stress_5","stress_6","stress_7","stress_8","stress_9","trauma_1","trauma_2","trauma_3","trauma_4","harm1_1","harm1_2","harm2_1","harm2_2","harm3","armor","heavy","special","ability1_check","ability1","ability2_check","ability2","ability3_check","ability3","ability4_check","ability4","ability5_check","ability5","ability6_check","ability6","ability7_check","ability7","ability8_check","ability8","ability9_check","ability9","ability10_check","ability10","ability11_check","ability11","ability12_check","ability12","playbook_xp1","playbook_xp2","playbook_xp3","playbook_xp4","playbook_xp5","playbook_xp6","playbook_xp7","playbook_xp8","insight_xp1","insight_xp2","insight_xp3","insight_xp4","insight_xp5","insight_xp6","prowess_xp1","prowess_xp2","prowess_xp3","prowess_xp4","prowess_xp5","prowess_xp6","resolve_xp1","resolve_xp2","resolve_xp3","resolve_xp4","resolve_xp5","resolve_xp6","doctor1","doctor2","doctor3","doctor4","hack1","hack2","hack3","hack4","rig1","rig2","rig3","rig4","study1","study2","study3","study4","helm1","helm2","helm3","helm4","scramble1","scramble2","scramble3","scramble4","scrap1","scrap2","scrap3","scrap4","sulk1","skulk2","skulk3","skulk4","attune1","attune2","attune3","attune4","command1","command2","command3","command4","consort1","consort2","consort3","consort4","sway1","sway2","sway3","sway4"}
    """
    
    self.id = raw["id"] + raw["playbook"]
    self.set_basic_vars(raw)
    
    self.insight = raw
    self.prowess = raw
    self.resolve = raw
    self.armor = raw

    # Still to implement
    
    #
    #self._trauma = trauma
    #self._harm = harm
    #self._healing = healing
    #self._abilities = abilities
    self.stress = self.get_total(raw, 9, "stress_")
    self.playbook_xp = self.get_total(raw, 8, "playbook_xp")

    self.abilities = []
    for i in range(12): #12 possible abilities
      if (raw["ability"+str(i+1)+"_check"] is not None and raw["ability"+str(i+1)] is not None):
        self.abilities.append(raw["ability"+str(i+1)].strip())
    
    return self

  def set_basic_vars(self, source):
    self.playbook = source["playbook"]
    self.name = source["name"]
    self.crew = source["crew"]
    self.alias = source["alias"]
    self.look = source["look"]
    self.heritage = source["heritage"]
    self.background = source["background"]
    self.vice = source["vice"]

  def __str__(self):
    abilities = str('\n\n'.join(self.abilities))

    return f"""
    **Name:** {self.name}
    **Crew:** {self.crew}
    **Alias:** {self.alias}
    **Look:** {self.look}
    **Heritage:** {self.heritage}
    **Background:** {self.background}
    **Vice:** {self.vice}

    **Playbook XP:** {self.num_to_dots(self.playbook_xp, 8)}

    {str(self._insight)}

    {str(self._prowess)}
    
    {str(self._resolve)}

    {str(self._armor)}
    
    **Abilities**
    {abilities}"""

  def __repr__(self):
    return self.to_dict()