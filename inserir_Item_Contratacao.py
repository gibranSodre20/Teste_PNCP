import integracao
import json
import conexao
import os

#Inserir itens contratação
json_data = None
token = conexao.get_token()
files = None #Não deve ser passado nada para inserir termos
endpoint = None

cnpj = os.getenv("cnpj_treinamento")

def inserirItensContratacao(ano, sequencial):
    endpoint = f"/v1/orgaos/{cnpj}/compras/{ano}/{sequencial}/itens"
   # Lê o conteúdo do arquivo JSON
    with open("https://raw.githubusercontent.com/gibranSodre20/Test_PNCP/refs/heads/master/Arquivos%20Json/inserirTermos.Json?token=GHSAT0AAAAAADEUY4RLIWPEN66U2R2YP55O2CHEQ7A", "r", encoding="utf-8") as f:
        json_data = f.read()
# Cabeçalhos
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "*/*",
        "Content-Type": "application/json"
        }    
    # Envia a requisição POST endpoint, json_data, headers, files, inserirContratacao
    #response = requests.post(url, headers=headers, data=json_data, verify=False)  # verify=False ignora o SSL
    response = integracao.executaEndPoint(endpoint, json_data, headers, files, False)
# Exibe a resposta
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    #Criar Json
    dados = response.json()
    # Acessa o valor do campo "path"
    caminho = dados["path"]
    #fatiar string pelo separador "/" e pegar o valor do ano e o sequencial
    ano = caminho.split("/")[6]
    sequencial = caminho.split("/")[7]
    print("ano: " + ano)
    print("sequencial: " + sequencial)


