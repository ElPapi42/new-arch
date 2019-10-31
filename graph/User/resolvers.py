from models.User import User

def all_users(root, info):
  return User.objects.all()
  
def single_user(self, info, **kwargs):
  id = kwargs.get('id')
  email = kwargs.get('email')

  if id is not None:
      return User.objects.get(pk=id)

  if email is not None:
      return User.objects.get(email=email)

  return None