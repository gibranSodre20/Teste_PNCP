import Plano_Contratacao


response = Plano_Contratacao.InserirPlanoContratacao()
print("Status Code:", response.status_code)
print("Response Body:", response.text)

