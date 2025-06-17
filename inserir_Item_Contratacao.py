import Integracao
import json
import Conexao
import os
import Buscar_json

#Inserir itens contratação
json_data = None
token = Conexao.get_token()
files = None #Não deve ser passado nada para inserir termos
endpoint = None

cnpj = os.getenv("cnpj_treinamento")
usuario_git = os.getenv("usuario_git")
repositorio = os.getenv("repositorio")

def inserirItensContratacao(ano, sequencial):
    endpoint = f"/v1/orgaos/{cnpj}/compras/{ano}/{sequencial}/itens"
   # Lê o conteúdo do arquivo JSON
    url_json = f"https://raw.githubusercontent.com/{usuario_git}/{repositorio}/refs/heads/main/Arquivos_Json/InserirItensContratacao.json"
    json_data = Buscar_json.buscar_json_raw(url_json)
      
# Cabeçalhos
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "*/*",
        "Content-Type": "application/json"
        }    
    # Envia a requisição POST endpoint, json_data, headers, files, inserirContratacao
    #response = requests.post(url, headers=headers, data=json_data, verify=False)  # verify=False ignora o SSL
    response = Integracao.executa_endpoint(endpoint, json.dumps(json_data, indent=4), headers, files, False)
# Exibe a resposta
    
    return response


