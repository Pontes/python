"""
 executar o servidor para o teste
 python -m http.server 8000
"""
from flask import Flask,render_template, request, redirect, session, flash, url_for
#from flask_mysqldb import MySQL
from models import Jogo, Usuario

from dao import JogoDao

app = Flask(__name__)
app.secret_key = 'alura'

"""app.config['MYSQL_HOST'] = "0.0.0.0"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "admin"
app.config['MYSQL_DB'] = "jogoteca"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)
jogo_dao = JogoDao(db)"""


usuario1 = Usuario('pj', 'Pontes', 'pwd')
usuario2 = Usuario('manu', 'Emanuelle', 'marley123')
usuario3 = Usuario('dog', 'Marley', '123456')

users = {usuario1.id: usuario1,
         usuario2.id: usuario2,
         usuario3.id: usuario3}

jogo1 = Jogo('Super Mario', 'ação', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
jogo3 = Jogo('Mortal Kombat', 'FIGHT', 'SNES')
lista = [jogo1, jogo2, jogo3]

@app.route('/')
def index():
    lnk = '/novo'
    return render_template('lista.html', titulo='Meus Jogos Sinistros', jogos=lista, link = lnk)

@app.route('/novo')
def novo():
    # if 'usuario_logado' not in session or session['usuario_logado'] == None:
    #     return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    #jogo_dao.salvar(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in users:
        user = users[request.form['usuario']]
        if user.senha == request.form['senha']:
            session['usuario_logado'] = user.id
            flash(user.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Login ou Senha inválidos! tente novamente!')
            return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash("Nenhum usuário logado")
    return redirect(url_for('index'))

app.run(debug=True)