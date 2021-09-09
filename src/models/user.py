from datetime import datetime

class User():

  def __init__(self, id=None, active_character=None):
    self.id = id
    self.active_character = active_character
    self.updated_at = datetime.now()
    self.created_at = datetime.now()

  
  def from_dict(self, source: dict):
    self.id = source["id"]
    self.active_character = source["data"]["active_character"]
    self.updated_at = source["meta"]["updated_at"]
    self.created_at = source["meta"]["created_at"]
    
    return self
    

  def to_dict(self):
    return {
      "id": self.id,
      "data": {
        "active_character": self.active_character
      },
      "meta": {
        "created_at": self.created_at,
        "updated_at": self.updated_at
      }
    }

  def __str__(self):
    return str(self.to_dict())

  def __repr__(self):
    return self.to_dict()