import Integracao
import Conexao

#Inserir termo
endpoint = "/v1/orgaos/49238155000150/contratos/2025/4/termos"
json_data = "null"
token = Conexao.getToken()
files = "" #Não deve ser passado nada para inserir termos

# Lê o conteúdo do arquivo JSON
with open("D:\PROJETO_PNCP\Arquivos Json\inserirTermos.json", "r", encoding="utf-8") as f:
    json_data = f.read()

# Cabeçalhos
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "*/*",
    "Content-Type": "application/json"
        }
    
# Envia a requisição POST endpoint, json_data, headers, files, inserirContratacao
#response = requests.post(url, headers=headers, data=json_data, verify=False)  # verify=False ignora o SSL
response = Integracao.executaEndPoint(endpoint, json_data, headers, files, False)
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


