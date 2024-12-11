import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import User

class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(self, info):
        # Devuelve todos los usuarios desde la base de datos
        return User.query.all()

schema = graphene.Schema(query=Query)
