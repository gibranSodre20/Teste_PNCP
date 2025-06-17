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
    data_hora = f"{datetime.now().strftime("%Y-%m-%dT%H:%M:%S")}"
    json_ata["numeroAtaRegistroPreco"] = data_hora.replace("-", "").replace(":", "").replace(".", "").replace(" ", "")
    json_ata["anoAta"] = anoCompra
    json_ata["dataAssinatura"] = f"{anoCompra}-07-21" 
    json_ata["dataVigenciaInicio"] = f"{anoCompra}-07-21" 
    json_ata["dataVigenciaFim"] = f"{int(anoCompra) + 1}-07-21"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "*/*",
        "Content-Type": "application/json"
        }
    response = integracao.executa_endpoint(endpoint, json.dumps(json_ata, indent=4), headers, files, False)
    return response
    