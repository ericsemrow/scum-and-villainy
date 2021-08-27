import discord
from src.uses_dice import UsesDice
class Action(UsesDice):
  description = None
  roll_result = {
    1: "Bad outcome",
    2: "Bad outcome",
    3: "Bad outcome",
    4: "Success with complications",
    5: "Success with complications",
    6: "Success",
    7: "Crit!"
  }

 
  def getRoll(self):
    result = self.roll()
    msg = self.roll_result[result.total]
    # if 6 check for crit
    if( result.total == 6 and self.num_die != 0 ):
      sixes = self.getNumSixes(result)
      if( sixes > 1):
        msg = self.roll_result[7]
    
    return f"{str(result)}: {msg}"
        

