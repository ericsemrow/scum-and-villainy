from src.models.firestore import Firestore
from src.models.user import User

class UserRepository(Firestore):

  col = u'users'

  def get_user_or_create(self, user_id):
    doc = self.get_user_ref(user_id).get()

    if doc.exists:
      return User().from_dict( doc.to_dict() )
    else:
      user = User(id=user_id)
      self.get_user_ref(user_id).set(user.to_dict())
      return user

  def store_user(self, user: User):
    self.get_user_ref(user.id).set(user.to_dict())

  def get_user_ref( self, user_id ):
    return self.db.collection(self.col).document(str(user_id))