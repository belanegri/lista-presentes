from flask import Flask, render_template, redirect, request, url_for, flash
from models import db, Presente

app = Flask(__name__)

# Configurações
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///presentes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sua_chave_secreta_aqui'

# Inicialização do banco de dados
db.init_app(app)

# Criação automática das tabelas
with app.app_context():
    db.create_all()


# Rota principal - lista de presentes
@app.route('/')
def index():
    presentes = Presente.query.order_by(Presente.id).all()
    return render_template('index.html', presentes=presentes)


# Rota para escolher um presente
@app.route('/escolher_presente', methods=['POST'])
def escolher_presente():
    presente_id = request.form.get('presente_id')
    nome = request.form.get('nome_comprador', '').strip()
    telefone = request.form.get('telefone_comprador', '').strip()
    quantidade = request.form.get('quantidade')

    # Validação de campos
    if not presente_id or not nome or not telefone or not quantidade:
        flash('Todos os campos são obrigatórios.', 'error')
        return redirect(url_for('index'))

    try:
        quantidade = int(quantidade)
        if quantidade < 1:
            raise ValueError
    except ValueError:
        flash('A quantidade deve ser um número inteiro maior que zero.', 'error')
        return redirect(url_for('index'))

    presente = Presente.query.get(presente_id)
    if not presente:
        flash('Presente não encontrado.', 'error')
        return redirect(url_for('index'))

    if presente.foi_escolhido:
        flash('Este presente já foi escolhido.', 'error')
        return redirect(url_for('index'))

    # Atualiza o presente
    presente.foi_escolhido = True
    presente.nome_comprador = nome
    presente.telefone_comprador = telefone
    presente.quantidade = quantidade

    db.session.commit()
    flash('Presente escolhido com sucesso!', 'success')
    return redirect(url_for('index'))


# Rota para cancelar escolha
@app.route('/cancelar_escolha/<int:presente_id>', methods=['POST'])
def cancelar_escolha(presente_id):
    presente = Presente.query.get(presente_id)
    if presente and presente.foi_escolhido:
        presente.foi_escolhido = False
        presente.nome_comprador = None
        presente.telefone_comprador = None
        presente.quantidade = None
        db.session.commit()
        flash('Escolha cancelada com sucesso!', 'success')
    else:
        flash('Não foi possível cancelar a escolha.', 'error')
    return redirect(url_for('index'))


# Área administrativa
@app.route('/admin')
def admin():
    presentes = Presente.query.order_by(Presente.id).all()
    return render_template('admin.html', presentes=presentes)


# Rodar o servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

