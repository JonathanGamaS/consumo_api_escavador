from flask_api import FlaskAPI
from orchestration import key_generator, pesquisa_usuario

app = FlaskAPI(__name__)


@app.route('/api_key/')
def generate_api_key():
    credentials = key_generator()
    return credentials


@app.route('/pesquisa_usuario/{termo_pesquisa}')
def pesquisa_usuario_escavador(termo_pesquisa):
    result = pesquisa_usuario(termo_pesquisa)
    return result