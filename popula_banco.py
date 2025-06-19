from app import app, db
from models import Presente

itens = [
    # Cozinha – Utensílios e Ferramentas
    "Abridor de garrafas",
    "Abridor de latas",
    "Açucareiro",
    "Afiador de facas",
    "Batedor de ovos",
    "Colher para sorvete",
    "Concha",
    "Espátula para bolo",
    "Espremedor de alho",
    "Espremedor de batatas",
    "Espremedor de frutas",
    "Faca de pão",
    "Faquinhas de patê",
    "Fatiador de queijos",
    "Pegador de massas",
    "Ralador",
    "Rolo de abrir massa",
    "Saleiro",
    "Pimenteiro",
    "Paliteiro",
    "Suporte para filtro de café",
    "Suporte para sabão e detergente",
    "Tesoura comum",
    "Xícaras de medida",
    "Medidores de xícaras e colheres",
    "Timer de cozinha",
    "Avental",
    "Luvas térmicas",

    # Banheiro
    "Escova para vaso sanitário",
    "Lixeira para banheiro",
    "Tapete antiderrapante para box",
    "Tapete atoalhado para banheiro",
    "Toalhas de banho",
    "Toalhas de rosto",

    # Quarto
    "Cobertor",
    "Fronhas avulsas",
    "Jogo de cama",
    "Pegador de colchão",
    "Tábua de passar roupa",

    # Lavanderia e Limpeza
    "Balde com espremedor",
    "Rodo para chão",
    "Vassoura e pá",
    "Escova para roupas",
    "Cesto para roupas sujas",
    "Panos de chão",
    "Pano de prato",
    "Escova para lavar louça",

    # Diversos
    "Baldes de plástico",
    "Cabides",
    "Pá de lixo"
]

with app.app_context():
    for nome in itens:
        existe = Presente.query.filter_by(nome=nome).first()
        if not existe:
            p = Presente(nome=nome)
            db.session.add(p)
    db.session.commit()
    print("Itens adicionados ao banco com sucesso!")

exit()
