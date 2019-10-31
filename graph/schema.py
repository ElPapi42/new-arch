from graphene import Schema
from .user.query import Query as UserQuery

"""
ALL_QUERIES = schema_operations_builder(
    operationName='Query',
    operationModule='query',
    operationBase='BaseQuery',
    clsName='Query'
)"""


schema = Schema(query=UserQuery)