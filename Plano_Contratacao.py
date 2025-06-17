import Integracao
import json 
import os
import Conexao
import Buscar_json
from datetime import datetime

json_pca = None
token = Conexao.get_token()
files = None

cnpj = os.getenv("cnpj_treinamento")
usuario_git = os.getenv("usuario_git")
repositorio = os.getenv("repositorio") 


def inserirPlanoContratacao():
    ano = input("Informe o ano do PCA")
    endpoint = f"/v1/orgaos/{cnpj}/pca"
    url_json = f"https://raw.githubusercontent.com/{usuario_git}/{repositorio}/refs/heads/main/Arquivos_Json/InserirPCA.json"
    json_pca = Buscar_json.buscar_json_raw(url_json)
    #data_hora = datetime.now()
    json_pca["anoPca"] = ano
    json_pca["itensPlano"][0]["dataDesejada"] = f"{ano}-07-07"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "*/*",
        "Content-Type": "application/json"
        }    
    response = Integracao.executa_endpoint(endpoint, json.dumps(json_pca, indent =4), headers, files, False)
    return response 
