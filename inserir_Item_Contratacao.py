import integracao
import json
import conexao
import os
import buscar_json

#Inserir itens contratação
json_data = None
token = conexao.get_token()
files = None #Não deve ser passado nada para inserir termos
endpoint = None

cnpj = os.getenv("cnpj_treinamento")
usuario_git = os.getenv("usuario_git")
repositorio = os.getenv("repositorio")

def inserirItensContratacao(ano, sequencial):
    endpoint = f"/v1/orgaos/{cnpj}/compras/{ano}/{sequencial}/itens"
   # Lê o conteúdo do arquivo JSON
    url_json = f"https://raw.githubusercontent.com/{usuario_git}/{repositorio}/refs/heads/main/Arquivos_Json/InserirItensContratacao.json"
    json_data = buscar_json.buscar_json_raw(url_json)
      
# Cabeçalhos
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "*/*",
        "Content-Type": "application/json"
        }    
    # Envia a requisição POST endpoint, json_data, headers, files, inserirContratacao
    #response = requests.post(url, headers=headers, data=json_data, verify=False)  # verify=False ignora o SSL
    response = integracao.executa_endpoint(endpoint, json.dumps(json_data, indent=4), headers, files, False)
# Exibe a resposta
    if response:
        print("Status Code:", response.status_code)
        print("Response Body:", response.text)
    """#Criar Json
        dados = response.json()
    # Acessa o valor do campo "path"
        caminho = dados["path"]
    #fatiar string pelo separador "/" e pegar o valor do ano e o sequencial
        ano = caminho.split("/")[6]
        sequencial = caminho.split("/")[7]
        print("ano: " + ano)
        print("sequencial: " + sequencial)
"""

