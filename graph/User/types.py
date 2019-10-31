from graphene import String
from graphene_django.types import DjangoObjectType
from models.User import User

class UserType(DjangoObjectType):
  """User tokens"""
  class Meta:
    model = User
