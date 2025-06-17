import requests
import json

def buscar_arquivo_raw(url_arquivo):
 
    #url_raw = f"https://raw.githubusercontent.com/{usuario}/{repositorio}/{branch}/{caminho_arquivo}"
    
    try:
        response = requests.get(url_arquivo)
        response.raise_for_status()  # Levanta uma exceção para erros HTTP
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar o arquivo: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        return None

# --- Exemplo de uso ---
usuario_github = "octocat" # Substitua pelo seu usuário ou organização
repositorio_github = "Spoon-Knife" # Substitua pelo seu repositório
branch_github = "main" # Geralmente 'main' ou 'master'
caminho_do_arquivo_json = "data.json" # Substitua pelo caminho real do seu arquivo JSON
