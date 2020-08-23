import requests
import os
import json


def key_generator():
    try:
        email = os.getenv("email")
        senha = os.getenv("password")
        url = 'https://api.escavador.com/api/v1/request-token'
        request_body = {
            'username': email,  
            'password': senha 
        }
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json'
        }
        response = requests.post(url=url, data=json.dumps(request_body), headers=headers)
        response_dict = json.loads(response.content)
        dados_credenciais = {
            "access_token": response_dict["access_token"],
            "refresh_token": response_dict["refresh_token"]
        }
        return dados_credenciais
    except Exception as e:
        raise e


def pesquisa_usuario(termo_pesquisa):
    try:
        credenciais = key_generator()
        access_token = credenciais["access_token"]
        url = 'https://api.escavador.com/api/v1/busca'

        params = {
            'q': termo_pesquisa,  
            'qo': 't',  
            'page': '1'
        }

        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-Requested-With': 'XMLHttpRequest'
        }

        response = requests.get(url, headers=headers, params=params)
        resopnse_dict = json.loads(response.content)
        return resopnse_dict
    except Exception as e:
        raise e 
