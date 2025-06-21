from app import app, db
from models import Presente

itens = [
    # Cozinha – Utensílios e Ferramentas
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
    ("Cozinha", "Lixinho de pia"),
    ("Cozinha", "Potes"),
    ("Cozinha", "Vasilhas"),
    ("Cozinha", "Facas"),
    ("Cozinha", "Garfos"),
    ("Cozinha", "Colheres"),
    ("Cozinha", "Potes para arroz"),
    ("Cozinha", "Pote para café"),

    # Cozinha – Preparação e Armazenamento (novos)
    ("Cozinha", "Assadeira antiaderente"),
    ("Cozinha", "Bacias de plástico"),
    ("Cozinha", "Escorredor de arroz"),
    ("Cozinha", "Escorredor de macarrão"),
    ("Cozinha", "Escorredor de talheres"),
    ("Cozinha", "Forma para bolo"),
    ("Cozinha", "Forma para gelo"),
    ("Cozinha", "Forma para pizza"),
    ("Cozinha", "Frigideira pequena"),
    ("Cozinha", "Funil pequeno de plástico"),
    ("Cozinha", "Garrafa térmica"),
    ("Cozinha", "Jarra para água"),
    ("Cozinha", "Jarra para suco"),
    ("Cozinha", "Peneiras para culinária (P/M/G)"),
    ("Cozinha", "Porta-condimentos"),
    ("Cozinha", "Porta-temperos giratório ou magnético"),
    ("Cozinha", "Potes herméticos para mantimentos"),
    ("Cozinha", "Descanso de panela"),

    # Cozinha – Organização e Servir
    ("Cozinha", "Jogo porta-copos"),
    ("Cozinha", "Lixeira pequena para cozinha"),
    ("Cozinha", "Petisqueira"),
    ("Cozinha", "Porta-guardanapos"),
    ("Cozinha", "Suporte para papel toalha"),
    ("Cozinha", "Tábua para cortar alimentos"),
    ("Cozinha", "Tábua de frios"),
    ("Cozinha", "Toalha de mesa para uso diário"),

    # Banheiro
    ("Banheiro", "Escova para vaso sanitário"),
    ("Banheiro", "Lixeira para banheiro"),
    ("Banheiro", "Tapete antiderrapante para box"),
    ("Banheiro", "Tapete atoalhado para banheiro"),
    ("Banheiro", "Toalhas de banho"),
    ("Banheiro", "Toalhas de rosto"),

    # Quarto
    ("Quarto", "Cobertor"),
    ("Quarto", "Fronhas avulsas"),
    ("Quarto", "Jogo de cama"),
    ("Quarto", "Lençol"),
    ("Quarto", "Pegador de colchão"),
    ("Quarto", "Tábua de passar roupa"),

    # Lavanderia
    ("Lavanderia", "Baldes"),
    ("Lavanderia", "Rodo para chão"),
    ("Lavanderia", "Vassoura"),
    ("Lavanderia", "Pá"),
    ("Lavanderia", "Escova para roupas"),
    ("Lavanderia", "Cesto para roupas sujas"),
    ("Lavanderia", "Panos de chão"),
    ("Lavanderia", "Pano de prato"),
    ("Lavanderia", "Escova para lavar louça"),

    # Diversos
    ("Diversos", "Cabides"),
    ("Diversos", "Pá de lixo"),
    ("Diversos", "Baldes de plástico"),
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
