from app import app
from flask import render_template
from flask import request

@app.route('/') #Configurando uma rota web
@app.route('/index')
def index():
    return render_template('index.html', titulo="Quasar", nome="Daniel")

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contato", nome="Daniel")

@app.route('/comprar')
def comprar():
    return render_template('comprar.html', titulo="Comprar", nome="Daniel")

@app.route('/login')
def login():
    return render_template('login.html', titulo="Comprar", nome="Daniel")

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="Cadastro", nome="Daniel")

@app.route('/adquirir')
def adiquirir():
    return render_template('adiquirir.html', titulo="Adiquirir", nome="Daniel")

@app.route('/index2')
def index2():
    return render_template('index2.html', titulo="Audi RS6 Avant", nome="Daniel")

@app.route('/index3')
def index3():
    return render_template('index3.html', titulo="Audi RS6 Avant", nome="Daniel")

@app.route('/index4')
def index4():
    return render_template('index4.html', titulo="Audi RS6 Avant", nome="Daniel")

@app.route('/index5')
def index5():
    return render_template('index5.html', titulo="Audi RS6 Avant", nome="Daniel")

@app.route('/index6')
def index6():
    return render_template('index6.html', titulo="Audi RS6 Avant", nome="Daniel")

@app.route('/index7')
def index7():
    return render_template('index7.html', titulo="Audi RS6 Avant", nome="Daniel")

@app.route('/index8')
def index8():
    return render_template('index8.html', titulo="Audi RS6 Avant", nome="Daniel")

@app.route('/index9')
def index9():
    return render_template('index9.html', titulo="Audi RS6 Avant", nome="Daniel")

@app.route('/index10')
def index10():
    return render_template('index10.html', titulo="Audi RS6 Avant", nome="Daniel")