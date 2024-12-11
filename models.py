from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"
