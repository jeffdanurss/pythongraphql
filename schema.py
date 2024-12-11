import graphene

# Definir un tipo que represente un objeto
class Persona(graphene.ObjectType):
    nombre = graphene.String()
    edad = graphene.Int()

# Definir las consultas
class Query(graphene.ObjectType):
    # Definir una consulta que devuelve una lista de personas
    personas = graphene.List(Persona)

    def resolve_personas(self, info):
        # Datos de ejemplo
        return [
            Persona(nombre="Juan", edad=25),
            Persona(nombre="María", edad=30),
            Persona(nombre="Carlos", edad=35)
        ]

# Crear el esquema de GraphQL
schema = graphene.Schema(query=Query)
