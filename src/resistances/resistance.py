from src.uses_dice import UsesDice
class Resistance(UsesDice):
  roll_result = {
    1: "Ouch. Mark 5 stress.",
    2: "Mark 4 stress.",
    3: "Mark 3 stress.",
    4: "Mark 2 stress.",
    5: "Mark 1 stress.",
    6: "No stress at all.",
    7: "Crit! Clear one stress."
  }

  
  def getRoll(self):
    result = self.roll()
    stress_cost = 6 - result.total
    msg = self.roll_result[result.total]
    # if 6 check for crit
    if( result.total == 6 and self.num_die != 0 ):
      sixes = self.getNumSixes(result)
      if( sixes > 1):
        msg = self.roll_result[7]
    
    return f"{str(result)}: {msg}"
        

