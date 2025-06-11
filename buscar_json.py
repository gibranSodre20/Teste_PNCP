import requests
import json


def buscar_json_raw(url_raw):
    
    try:
        response = requests.get(url_raw)
        response.raise_for_status()  # Levanta uma exceção para erros HTTP
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar o arquivo: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        return None

def buscar_documento_raw(url_documento):
    
    response = requests.get(url_documento)

    if response.status_code == 200:
        with open("arquivo_baixado.pdf", "wb") as f:
            f.write(response.content)
            print(type(f))
            return f.BytesIO()
        print("Arquivo PDF salvo com sucesso!")
    else:
        print(f"Erro ao baixar o arquivo: {response.status_code}")
    
    """
    if response.status_code == 200:
    data = response.json()
    pdf_files = [item['path'] for item in data['tree'] if item['path'].endswith('.pdf')]
    
    print("Arquivos PDF encontrados:")
    for pdf in pdf_files:
        print(f"https://github.com/{owner}/{repo}/blob/{branch}/{pdf}")
else:
    print(f"Erro ao acessar o repositório: {response.status_code}")
    """