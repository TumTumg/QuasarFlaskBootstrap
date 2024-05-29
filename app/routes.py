from app import app
from flask import render_template, request
import json
import requests
from flask import session

link = "https://flaskti18nzmbotti-default-rtdb.firebaseio.com/" # Conecta o banco

@app.route('/') # Configurando uma rota web
@app.route('/index')
def index():
    return render_template('index.html', titulo="Quasar", nome="Daniel")

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contato", nome="Daniel")

@app.route('/comprar')
def comprar():
    return render_template('comprar.html', titulo="Comprar", nome="Daniel")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            usuario = request.form.get("usuario")
            senha = request.form.get("senha")
            # Obtém os dados do usuário do banco de dados
            requisicao = requests.get(f'{link}/cadastrar/.json')
            dicionario = requisicao.json()

            for user_id, user_data in dicionario.items():
                if user_data.get('usuario') == usuario and user_data.get('senha') == senha:
                    return 'Login bem-sucedido!'

            return 'Usuário ou senha incorretos.'
        except Exception as e:
            return f'Ocorreu um erro\n\n + {e}'
    return render_template('login.html', titulo="Login", nome="Daniel")

@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrar_usuario():
    try:
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        telefone = request.form.get("telefone")
        idade = request.form.get("idade")
        cep = request.form.get("cep")
        dados = {"usuario": usuario, "senha": senha, "telefone": telefone, "idade": idade, "cep": cep}
        requisicao = requests.post(f'{link}/cadastrar/.json', data=json.dumps(dados))
        return 'Cadastrado com sucesso!'
    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'


USUARIO_ADM = "decaudas@gmail.com"
SENHA_ADM = "danielzinho"
@app.route('/loginAdm', methods=['GET', 'POST'])
def loginAdm():
    if request.method == 'POST':
        try:
            usuario = request.form.get("usuario")
            senha = request.form.get("senha")

            # Verifica se o usuário e senha correspondem ao ADM
            if usuario == USUARIO_ADM and senha == SENHA_ADM:
                session['logged_in'] = True  # Define a sessão como logada
                return 'Login bem-sucedido! Você agora tem acesso ao CRUD.'
            else:
                return 'Usuário ou senha incorretos.'

        except Exception as e:
            return f'Ocorreu um erro\n\n + {e}'

    return render_template('loginAdm.html', titulo="Login ADM", nome="Daniel")


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="Cadastro", nome="Daniel")

@app.route('/adquirir')
def adquirir():
    return render_template('adquirir.html', titulo="Adquirir", nome="Daniel")

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

@app.route('/crud')
def crud():
    return render_template('crud.html', titulo="CRUD", nome="Daniel")

@app.route('/pagamento')
def pagamento():
    return render_template('pagamento.html', titulo="Pagamento", nome="Daniel")


@app.route('/listar')
def listar_tudo():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json') # Solicitar os dados que estão no banco
        dicionario = requisicao.json()
        return dicionario
    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'

@app.route('/listarIndividual')
def listar_individual():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json') # Solicitar os dados que estão no banco
        dicionario = requisicao.json()
        id_cadastro = ""
        for codigo in dicionario:
            usuario = dicionario[codigo]['usuario']
            if usuario == "Daniel Zambotti":
                id_cadastro = codigo
        return id_cadastro
    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'

@app.route('/atualizar')
def atualizar():
    try:
        dados = {"nome": "Gabriela"} # Parâmetro de atualização
        requisicao = requests.patch(f'{link}/cadastrar/-NySNSADmCFbENf0xj11/.json', data=json.dumps(dados))
        return "Atualizado com sucesso!"
    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'

@app.route('/excluir')
def excluir():
    try:
        requisicao = requests.delete(f'{link}/cadastrar/-NySNSADmCFbENf0xj11/.json')
        return "Excluído com sucesso"
    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'
