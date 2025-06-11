import integracao
import json
from dotenv import load_dotenv
import os
import conexao
import inserir_Item_Contratacao
import requests
import buscar_json
from datetime import datetime
from io import BytesIO

# Carrega variáveis do arquivo .env
load_dotenv()

token = conexao.get_token()
#Inserir Contratação
endpoint = f"/v1/orgaos/{os.getenv("cnpj_treinamento")}/compras"
json_data = "null"

usuario_git = os.getenv("usuario_git")
repositorio = os.getenv("repositorio")
caminho_objetoCompra = os.getenv("caminho_objetoCompra")
branch = os.getenv("branch")
url_raw = f"https://raw.githubusercontent.com/{usuario_git}/{repositorio}/refs/heads/master/Arquivos_Json/objetoCompra.json"

json_data = buscar_json.buscar_json_raw(url_raw)

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "*/*",
    "Titulo-Documento": "tituloDocumento",
    "Tipo-Documento-Id": "2"
}

arquivo_json = ""
#json_data_json = json.dumps(json_data, indent=4)
if json_data:
    arquivo_json = json.loads(json.dumps(json_data, indent=4))
    data_hora = f"{datetime.now()}"
    arquivo_json["numeroCompra"] = data_hora.replace("-", "").replace(":", "").replace(".", "").replace(" ", "")
else:
    print("Não foi possível obter o arquivo JSON.")
files = {
  # "compra": ("objetoCompra.json", open(r"D:\PROJETO_PNCP\Arquivos_Json\objetoCompra.json", "rb"), "application/json"),
    "compra": ("objetoCompra.json", json.dumps(arquivo_json, indent=4), "application/json"),
    "documento": ("Documento-teste-1.pdf", open(r"D:\PROJETO_PNCP\Arquivos_teste\Documento-teste-1.pdf", "rb"), "application/pdf")
}

# Envia a requisição POST
#response = requests.post(url, headers=headers, data=json_data, verify=False)  # verify=False ignora o SSL
response = integracao.executa_endpoint(endpoint, json.dumps(arquivo_json, indent=4), headers, files, True)
# Exibe a resposta
print("Status Code:", response.status_code)
print("Response Body:", response.text)


#Criar Json
dados = response.json()

# Acessa o valor do campo "path"
caminho = dados["compraUri"]
print("Path:", caminho)
#fatiar string pelo separador "/" e pegar o valor do ano e o sequencial
valores = caminho.split("/")
ano = caminho.split("/")[8]
sequencial = caminho.split("/")[9]
print(response.status_code)

if response.status_code == 201:
    inserir_Item_Contratacao.inserirItensContratacao(ano, sequencial)
