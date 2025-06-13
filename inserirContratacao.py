import integracao
import json
from dotenv import load_dotenv
import os
import conexao
import inserir_Item_Contratacao
import buscar_json
from datetime import datetime
from dateutil.relativedelta import relativedelta


# Carrega variáveis do arquivo .env
load_dotenv()

token = conexao.get_token()
endpoint = f"/v1/orgaos/{os.getenv("cnpj_treinamento")}/compras"
usuario_git = os.getenv("usuario_git")
repositorio = os.getenv("repositorio")
url_json = f"https://raw.githubusercontent.com/{usuario_git}/{repositorio}/refs/heads/main/Arquivos_Json/objetoCompra.json"
caminho_arquivo_compra = os.getenv("caminho_arquivo_compra")

json_data = buscar_json.buscar_json_raw(url_json)
#documento = buscar_json.buscar_documento_raw(url_documento)

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "*/*",
    "Titulo-Documento": "tituloDocumento",
    "Tipo-Documento-Id": "2"
}

try:
    #Gera e atribui o valor do "numeroCompra" com base na data,hora e minuto, tornando sempre um valor único
    if json_data:
        json_compra = json.loads(json.dumps(json_data, indent=4))
        data_hora = f"{datetime.now().strftime("%Y-%m-%dT%H:%M:%S")}"
        json_compra["numeroCompra"] = data_hora.replace("-", "").replace(":", "").replace(".", "").replace(" ", "")
        json_compra["anoCompra"] = data_hora[0:4]
        json_compra["dataAberturaProposta"] = data_hora
        data_somada = datetime.now() + relativedelta(months=2)
        json_compra["dataEncerramentoProposta"] = f"{data_somada.strftime("%Y-%m-%dT%H:%M:%S")}"
        files = {
            "compra": ("objetoCompra.json", json.dumps(json_compra, indent=4), "application/json"),
            "documento": ("Documento-teste-1.pdf", open(rf"{caminho_arquivo_compra}", "rb"), "application/pdf")
                }
        # Envia a requisição POST
        response = integracao.executa_endpoint(endpoint, json.dumps(json_compra, indent=4), headers, files, True)
       
        if response.status_code == 201:
             #Criar Json
            dados = response.json()
            # Acessa o valor do campo "path"
            caminho = dados["compraUri"]
            #fatiar string pelo separador "/" e pegar o valor do ano e o sequencial
            valores = caminho.split("/")
            ano = valores[8]
            sequencial = valores[9]
            inserir_Item_Contratacao.inserirItensContratacao(ano, sequencial)

    else:
        print("Não foi possível obter o arquivo JSON.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


