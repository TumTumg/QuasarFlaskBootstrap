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