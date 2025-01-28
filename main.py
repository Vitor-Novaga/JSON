# json = {
#     "nome": "Rafael",
#     "type": "Docente",
#     "nomes": ["Pedro", "Paulo", "Alex"]
# }
# print (json['nomes'])

# import http.client

# json = http.client.HTTPConnection('www.brasilapi.com.br/api/cep/v1/79110550')

# print (json)

import http.client
import json
import Menu as m

def print_json(object):
    if type(object) is list:
        for json_ in object:
            for key in json_.keys():
                print (f"{key} : {json_[key]}")

    elif type (object) is dict:
        for key in object.keys():
             print (f"{key} : {object[key]}")

def espaco (nome):
    return str (nome).replace(' ', '%20')

def api(url):    
    http_request = http.client.HTTPSConnection('brasilapi.com.br')
    http_request.request ("GET", url)
    response = http_request.getresponse()
    resposta_bytes = response.read()
    json_ = json.loads(resposta_bytes)
    return json_

while True:

    m.menu_inicial ()

    op = int (input ("Digite a opção desejada: "))
    if op == 1:
        cidade = espaco (input ("Digite a cidade: "))
        json_cidade = api (f"/api/cptec/v1/cidade/{cidade}")
        print_json (json_cidade)

    elif op == 2:
        ano = input ("Digite o ano: ")
        json_ano = api(f"/api/feriados/v1/{ano}")
        print_json (json_ano)

    elif op == 3:    
        cep = input ("Digite o CEP: ")
        json_cep = api(f"/api/cep/v1/{cep}")
        print_json (json_cep)
    
    elif op == 4:
        ddd = input ("Digite o DDD: ")
        json_ddd = api(f"/api/ddd/v1/{ddd}")
        print_json (json_ddd)
    elif op == 5:
        cnpj = input("Digite o CNPJ: ")
        json_cnpj = api(f"/api/cnpj/v1/{cnpj}")
        print_json (json_cnpj)

    else:
        ("Opção inválida!")

        
