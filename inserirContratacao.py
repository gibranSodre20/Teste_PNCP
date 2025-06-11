import integracao
import json
from dotenv import load_dotenv
import os
import conexao
import inserir_Item_Contratacao
import buscar_json
from datetime import datetime


# Carrega variáveis do arquivo .env
load_dotenv()

token = conexao.get_token()
endpoint = f"/v1/orgaos/{os.getenv("cnpj_treinamento")}/compras"
usuario_git = os.getenv("usuario_git")
repositorio = os.getenv("repositorio")
url_json = f"https://raw.githubusercontent.com/{usuario_git}/{repositorio}/refs/heads/main/Arquivos_Json/objetoCompra.json"
#url_documento = f"https://raw.githubusercontent.com/{usuario_git}/{repositorio}/master/Arquivos_teste/Documento_teste_1.pdf"
 

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
        data_hora = f"{datetime.now()}"
        json_compra["numeroCompra"] = data_hora.replace("-", "").replace(":", "").replace(".", "").replace(" ", "")
        files = {
            "compra": ("objetoCompra.json", json.dumps(json_compra, indent=4), "application/json"),
            "documento": ("Documento-teste-1.pdf", open(r"D:\Teste_PNCP\Arquivos_teste\Documento_teste_1.pdf", "rb"), "application/pdf")
                }
        # Envia a requisição POST
        response = integracao.executa_endpoint(endpoint, json.dumps(json_compra, indent=4), headers, files, True)
        #Criar Json
        dados = response.json()
        # Acessa o valor do campo "path"
        caminho = dados["compraUri"]
        #fatiar string pelo separador "/" e pegar o valor do ano e o sequencial
        valores = caminho.split("/")
        ano = caminho.split("/")[8]
        sequencial = caminho.split("/")[9]
        if response.status_code == 201:
            inserir_Item_Contratacao.inserirItensContratacao(ano, sequencial)

    else:
        print("Não foi possível obter o arquivo JSON.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


