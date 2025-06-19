from app import app, db
from models import Presente

itens = [
    ("Cozinha", "Abridor de garrafas"),
    ("Cozinha", "Abridor de latas"),
    ("Cozinha", "Açucareiro"),
    ("Cozinha", "Afiador de facas"),
    ("Cozinha", "Batedor de ovos"),
    ("Cozinha", "Colher para sorvete"),
    ("Cozinha", "Concha"),
    ("Cozinha", "Espátula para bolo"),
    ("Cozinha", "Espremedor de alho"),
    ("Cozinha", "Espremedor de batatas"),
    ("Cozinha", "Espremedor de frutas"),
    ("Cozinha", "Faca de pão"),
    ("Cozinha", "Faquinhas de patê"),
    ("Cozinha", "Fatiador de queijos"),
    ("Cozinha", "Pegador de massas"),
    ("Cozinha", "Ralador"),
    ("Cozinha", "Rolo de abrir massa"),
    ("Cozinha", "Saleiro"),
    ("Cozinha", "Pimenteiro"),
    ("Cozinha", "Paliteiro"),
    ("Cozinha", "Suporte para filtro de café"),
    ("Cozinha", "Suporte para sabão e detergente"),
    ("Cozinha", "Tesoura comum"),
    ("Cozinha", "Xícaras de medida"),
    ("Cozinha", "Medidores de xícaras e colheres"),
    ("Cozinha", "Timer de cozinha"),
    ("Cozinha", "Avental"),
    ("Cozinha", "Luvas térmicas"),

    ("Banheiro", "Escova para vaso sanitário"),
    ("Banheiro", "Lixeira para banheiro"),
    ("Banheiro", "Tapete antiderrapante para box"),
    ("Banheiro", "Tapete atoalhado para banheiro"),
    ("Banheiro", "Toalhas de banho"),
    ("Banheiro", "Toalhas de rosto"),

    ("Quarto", "Cobertor"),
    ("Quarto", "Fronhas avulsas"),
    ("Quarto", "Jogo de cama"),
    ("Quarto", "Pegador de colchão"),
    ("Quarto", "Tábua de passar roupa"),

    ("Lavanderia", "Balde com espremedor"),
    ("Lavanderia", "Rodo para chão"),
    ("Lavanderia", "Vassoura e pá"),
    ("Lavanderia", "Escova para roupas"),
    ("Lavanderia", "Cesto para roupas sujas"),
    ("Lavanderia", "Panos de chão"),
    ("Lavanderia", "Pano de prato"),
    ("Lavanderia", "Escova para lavar louça"),

    ("Diversos", "Baldes de plástico"),
    ("Diversos", "Cabides"),
    ("Diversos", "Pá de lixo")
]

with app.app_context():
    for categoria, nome in itens:
        existe = Presente.query.filter_by(nome=nome).first()
        if not existe:
            p = Presente(nome=nome, categoria=categoria)
            db.session.add(p)
    db.session.commit()
    print("Itens adicionados ao banco com sucesso!")

exit()
