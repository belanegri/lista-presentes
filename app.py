from flask import Flask, render_template, redirect, request, url_for, flash
from models import db, Presente, Escolha

app = Flask(__name__)

# Configurações
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///presentes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sua_chave_secreta_aqui'

db.init_app(app)

# Criação automática das tabelas
with app.app_context():
    db.create_all()

# Rota principal
@app.route('/')
def index():
    presentes = Presente.query.order_by(Presente.id).all()
    return render_template('index.html', presentes=presentes)

# Rota para escolher presente
@app.route('/escolher_presente/<int:presente_id>', methods=['GET', 'POST'])
def escolher_presente(presente_id):
    presente = Presente.query.get_or_404(presente_id)

    if request.method == 'POST':
        nome = request.form.get('nome_comprador', '').strip()
        telefone = request.form.get('telefone_comprador', '').strip()
        quantidade = request.form.get('quantidade')

        if not nome or not quantidade:
            flash('Todos os campos são obrigatórios.', 'error')
            return redirect(url_for('index'))

        try:
            quantidade = int(quantidade)
            if quantidade < 1:
                raise ValueError
        except ValueError:
            flash('A quantidade deve ser um número inteiro maior que zero.', 'error')
            return redirect(url_for('index'))

        nova_escolha = Escolha(
            presente_id=presente.id,
            nome_comprador=nome,
            telefone_comprador=telefone,
            quantidade=quantidade
        )
        db.session.add(nova_escolha)
        db.session.commit()
        flash('Escolha registrada com sucesso!', 'success')
        return redirect(url_for('index'))

    return render_template('escolher.html', presente=presente)

# Área administrativa
@app.route('/admin')
def admin():
    presentes = Presente.query.order_by(Presente.id).all()
    return render_template('admin.html', presentes=presentes)

# Rodar o servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
