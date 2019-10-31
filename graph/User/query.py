from graphene import List, Field, String

from graph.base import BaseQuery
from types import UserType
from . import resolvers as resolve


class Query(BaseQuery):
    user = Field(
      UserType,
      email=String(),
      description="Single user.",
      resolver=resolve.single_user
    )

    users = List(
      UserType,
      description="A list of users.",
      resolver=resolve.all_users
    )