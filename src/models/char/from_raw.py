class FromRaw(object):
  
  filled_dots = {
    1: "❶",
    2: "❷",
    3: "❸",
    4: "❹",
    5: "❺",
    6: "❻",
    7: "❼",
    8: "❽",
    9: "❾",
  }
  empty_dots = {
    1: "①",
    2: "②",
    3: "③",
    4: "④",
    5: "⑤",
    6: "⑥",
    7: "⑦",
    8: "⑧",
    9: "⑨",
  }

  checked_dot = "☒"
  unchecked_dot = "☐"

  arrow_dot = "▶"

  def get_total(self, source, num_iterations, title):
    counter = 0
    for i in range(num_iterations): #6 possible xp
      if source[title+str(i+1)] is not None:
        counter += 1
    
    return counter
  
  def num_to_dots( self, val, possible ):
    string = ""
    for i in range(possible):
      string += self.filled_dots[i+1] if i < val else self.empty_dots[i+1]
    
    return string

  def bool_to_dot( self, val: bool):
    return self.checked_dot if val else self.unchecked_dot
  
  def num_to_arrows(self, val):
    string = ""
    for i in range(val):
      string += self.arrow_dot
    
    return string