from flask import Flask, render_template, redirect, url_for
from models import db, Presente

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///presentes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'chave-secreta'

db.init_app(app)

# Criação inicial do banco de dados
@app.before_first_request
def cria_banco():
    db.create_all()
    if Presente.query.count() == 0:
        itens = [
            "Abridor de garrafas", "Abridor de latas", "Açucareiro", "Afiador de facas", "Batedor de ovos",
            "Colher para sorvete", "Concha", "Espátula para bolo", "Espremedor de alho", "Espremedor de batatas",
            "Espremedor de frutas", "Faca de pão", "Faquinhas de patê", "Fatiador de queijos", "Pegador de massas",
            "Ralador", "Rolo de abrir massa", "Saleiro / Pimenteiro / Paliteiro", "Suporte para filtro de café",
            "Suporte para sabão e detergente", "Tesoura comum", "Xícaras de medida", "Medidores de xícaras e colheres",
            "Timer de cozinha", "Avental", "Luvas térmicas", "Assadeira antiaderente", "Bacias de plástico",
            "Escorredor de arroz", "Escorredor de macarrão", "Escorredor de talheres", "Forma para bolo",
            "Forma para gelo", "Forma para pizza", "Frigideira pequena", "Funil pequeno de plástico",
            "Garrafa térmica", "Jarra para água", "Jarra para suco", "Peneiras para culinária (P/M/G)",
            "Porta-condimentos", "Porta-temperos giratório ou magnético", "Potes herméticos para mantimentos",
            "Descanso de panela", "Jogo porta-copos", "Lixeira pequena para cozinha", "Petisqueira",
            "Porta-guardanapos", "Suporte para papel toalha", "Tábua para cortar alimentos", "Tábua de frios",
            "Toalha de mesa para uso diário", "Escova para vaso sanitário", "Lixeira para banheiro",
            "Tapete antiderrapante para box", "Tapete atoalhado para banheiro", "Toalhas de banho", "Toalhas de rosto",
            "Cobertor", "Fronhas avulsas", "Jogo de cama", "Pegador de colchão", "Tábua de passar roupa",
            "Balde com espremedor", "Rodo para chão", "Vassoura e pá", "Escova para roupas",
            "Cesto para roupas sujas", "Panos de chão", "Pano de prato", "Escova para lavar louça",
            "Baldes de plástico", "Cabides", "Pá de lixo"
        ]
        for item in itens:
            db.session.add(Presente(nome=item))
        db.session.commit()

@app.route('/')
def index():
    presentes = Presente.query.all()
    return render_template('index.html', presentes=presentes)

@app.route('/escolher/<int:id>')
def escolher_presente(id):
    presente = Presente.query.get(id)
    if presente and not presente.escolhido:
        presente.escolhido = True
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/admin')
def admin():
    presentes = Presente.query.all()
    return render_template('admin.html', presentes=presentes)

if __name__ == '__main__':
    app.run(debug=True)
