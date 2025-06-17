import integracao
import json
import conexao
import os
import buscar_json
from datetime import datetime
from dateutil.relativedelta import relativedelta

json_data = None
token = conexao.get_token()
files = None
endpoint = None

cnpj = os.getenv ("cnpj_treinamento")
usuario_git = os.getenv ("usuario_git")
repositorio = os.getenv ("repositorio")

def InserirAta(anoCompra, sequencialCompra):
    endpoint = f"/v1/orgaos/{cnpj}/compras/{anoCompra}/{sequencialCompra}/atas"

    url_json = f"https://raw.githubusercontent.com/{usuario_git}/{repositorio}/refs/heads/main/Arquivos_Json/InserirAta.json"
    json_ata = buscar_json.buscar_json_raw(url_json)
    data_hora = datetime.now()
    json_ata = ["numeroAtaRegistroPreco"] = data_hora[0:4]
    json_ata["anoAta"] = anoCompra

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "*/*",
        "Content-Type": "application/json"
        }
    response = integracao.executa_endpoint(endpoint, json.dumps(json_ata, indent=4), headers, files, False)

    if response:
        print("Status Code: ", response.status_code)
        print("Response Body: ", response.text)