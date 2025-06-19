from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Presente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    foi_escolhido = db.Column(db.Boolean, default=False)
    nome_comprador = db.Column(db.String(100), nullable=True)
    telefone_comprador = db.Column(db.String(20), nullable=True)
    quantidade = db.Column(db.Integer, nullable=True)
