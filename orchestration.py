import requests
import os
import json


def key_generator():
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
    response = requests.request('POST', url, headers=headers, json=payload)
    response_dict = json.loads(response.text)