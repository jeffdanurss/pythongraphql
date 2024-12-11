# app.py
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schema import schema  # Importamos el esquema desde schema.py

# Crear la aplicación FastAPI
app = FastAPI()

# Crear el router de GraphQL
graphql_app = GraphQLRouter(schema)

# Incluir el router en FastAPI bajo el prefijo /graphql
app.include_router(graphql_app, prefix="/graphql")

# Ruta raíz para saber que el servidor está corriendo
@app.get("/")
async def root():
    return {"message": "¡Bienvenido servidor graphql funcionando!"}
