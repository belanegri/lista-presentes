from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Presente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    total_escolhido = db.Column(db.Integer, default=0)
    quem_escolheu = db.Column(db.String(200), default='')  # nomes separados por vírgula

    escolhas = db.relationship('Escolha', backref='presente', lazy=True)


class Escolha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    presente_id = db.Column(db.Integer, db.ForeignKey('presente.id'), nullable=False)
    nome_comprador = db.Column(db.String(100), nullable=False)
    telefone_comprador = db.Column(db.String(20))
    quantidade = db.Column(db.Integer, nullable=False)
