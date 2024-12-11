from flask import Flask
from flask_graphql import GraphQLView
from models import db
from schema import schema

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Usamos SQLite para este ejemplo
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def home():
    return "¡Hola, mundo!"
# Crear la base de datos si no existe
with app.app_context():
    db.create_all()

# Definir la vista GraphQL
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)
