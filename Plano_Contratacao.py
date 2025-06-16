import integracao
import json 
import os
import conexao
import buscar_json
from datetime import datetime

json_pca = None
token = conexao.get_token()
files = None

cnpj = os.getenv("cnpj_treinamento")
usuario_git = os.getenv("usuario_git")
repositorio = os.getenv("repositorio") 


def InserirPlanoContratacao():
    ano = input("Informe o ano do PCA")
    endpoint = f"/v1/orgaos/{cnpj}/pca"
    url_json = f"https://raw.githubusercontent.com/{usuario_git}/{repositorio}/refs/heads/main/Arquivos_Json/InserirPCA.json"
    json_pca = buscar_json.buscar_json_raw(url_json)
    data_hora = datetime.now()
    json_pca["anoPca"] = ano
    json_pca["itensPlano"][0]["dataDesejada"] = f"{ano}-07-07"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "*/*",
        "Content-Type": "application/json"
        }    
    response = integracao.executa_endpoint(endpoint, json.dumps(json_pca, indent =4), headers, files, False)
    return response 
