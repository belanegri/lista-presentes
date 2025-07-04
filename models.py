from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Presente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)

    escolhas = db.relationship('Escolha', backref='presente', lazy=True)

    # Atributos calculados em tempo de execução
    total_escolhido = 0
    quem_escolheu = ''

class Escolha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    presente_id = db.Column(db.Integer, db.ForeignKey('presente.id'), nullable=False)
    nome_comprador = db.Column(db.String(100), nullable=False)
    telefone_comprador = db.Column(db.String(20))
    quantidade = db.Column(db.Integer, nullable=False)
