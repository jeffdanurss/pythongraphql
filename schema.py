# schema.py
import strawberry

# Definir un tipo que represente un objeto
@strawberry.type
class Persona:
    nombre: str
    edad: int

# Definir las consultas
@strawberry.type
class Query:
    @strawberry.field
    def personas(self) -> list[Persona]:
        # Datos de ejemplo
        return [
            Persona(nombre="Juan", edad=25),
            Persona(nombre="María", edad=30),
            Persona(nombre="Carlos", edad=35)
        ]

# Crear el esquema de GraphQL
schema = strawberry.Schema(query=Query)
