from flask_api import FlaskAPI
from orchestration import key_generator

app = FlaskAPI(__name__)


@app.route('/api_key/')
def generate_api_key():
    return 