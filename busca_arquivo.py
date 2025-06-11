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

# Crie um arquivo data.json de exemplo no seu repositório para testar
# Ex: Conteúdo de data.json: {"nome": "Teste", "valor": 123}

#dados_json = buscar_json_raw(usuario_github, repositorio_github, branch_github, caminho_do_arquivo_json)
"""
if dados_json:
    print("Conteúdo do JSON:")
    print(dados_json)
    print(f"Valor de 'nome': {dados_json.get('nome')}")
else:
    print("Não foi possível obter o arquivo JSON.")
"""