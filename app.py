from flask import Flask, render_template, redirect, request, url_for, flash, session
from models import db, Presente, Escolha
from collections import defaultdict

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///presentes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sua_chave_secreta_aqui'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    presentes = Presente.query.order_by(Presente.id).all()
    categorias = defaultdict(list)

    for presente in presentes:
        total_escolhido = sum(e.quantidade for e in presente.escolhas)
        quem_escolheu = ", ".join({e.nome_comprador for e in presente.escolhas if e.nome_comprador})

        presente.total_escolhido = total_escolhido
        presente.quem_escolheu = quem_escolheu
        categorias[presente.categoria].append(presente)

    return render_template('index.html', categorias=categorias)

@app.route('/escolher_presente/<int:presente_id>', methods=['GET', 'POST'])
def escolher_presente(presente_id):
    presente = Presente.query.get_or_404(presente_id)

    if request.method == 'POST':
        nome = request.form.get('nome_comprador', '').strip()
        telefone = request.form.get('telefone_comprador', '').strip()
        quantidade = request.form.get('quantidade')

        if not nome or not quantidade:
            flash('Por favor, preencha nome e quantidade.', 'error')
            return redirect(url_for('escolher_presente', presente_id=presente_id))

        try:
            quantidade = int(quantidade)
            if quantidade < 1:
                raise ValueError
        except ValueError:
            flash('Quantidade deve ser um número inteiro maior que zero.', 'error')
            return redirect(url_for('escolher_presente', presente_id=presente_id))

        # Salvar em sessão temporária
        session['dados_escolha'] = {
            'presente_id': presente_id,
            'nome': nome,
            'telefone': telefone,
            'quantidade': quantidade
        }

        return redirect(url_for('confirmar_presente'))

    return render_template('escolher.html', presente=presente)

@app.route('/confirmar_presente', methods=['GET', 'POST'])
def confirmar_presente():
    dados = session.get('dados_escolha')
    if not dados:
        flash('Nenhuma escolha em andamento.', 'error')
        return redirect(url_for('index'))

    presente = Presente.query.get_or_404(dados['presente_id'])

    if request.method == 'POST':
        escolha = Escolha(
            presente_id=presente.id,
            nome_comprador=dados['nome'],
            telefone_comprador=dados['telefone'],
            quantidade=int(dados['quantidade'])
        )
        db.session.add(escolha)
        db.session.commit()
        session.pop('dados_escolha', None)

        flash('Escolha confirmada com sucesso!', 'success')
        return redirect(url_for('index'))

    return render_template('confirmar.html', presente=presente, dados=dados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
