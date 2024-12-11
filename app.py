from flask import Flask
from flask_graphql import GraphQLView
from schema import schema

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Configurar la ruta /graphql para manejar las peticiones GraphQL
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
