from app import app, db
from models import Presente

itens = [
    # Lista de presentes (igual ao que você já tem)
    'Abridor de garrafas', 'Abridor de latas', 'Açucareiro', 'Afiador de facas',
    # ... (mantive o resto igual)
    'Toalhas de banho', 'Toalhas de rosto'
]

with app.app_context():
    Presente.query.delete()  # limpa a tabela
    for item in itens:
        presente = Presente(nome=item)
        db.session.add(presente)
    db.session.commit()

print("Todos os presentes foram adicionados com sucesso!")
