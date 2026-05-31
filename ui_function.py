import requests
import json


def consulta_cnpj(cnpj):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}
    response = requests.request("GET", url, params=querystring)

    resp = json.loads(response.text)

    return resp['cnpj'], resp['nome'], resp['telefone'], resp['email']


def consulta_cep(cep):
    url = f"https://h-apigateway.conectagov.estaleiro.serpro.gov.br/api-cep/v1/consulta/cep/{cep}"
    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}
    response = requests.request("GET", url, params=querystring)

    resp = json.loads(response.text)

    return resp['cnpj'], resp['nome'], resp['telefone'], resp['email']