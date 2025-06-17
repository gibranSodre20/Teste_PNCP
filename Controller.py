#import Plano_Contratacao 
import InserirAta

"""
response = Plano_Contratacao.inserirPlanoContratacao()
print("Status Code:", response.status_code)
print("Response Body:", response.text)

"""

response = InserirAta.inserirAta(2030, 1)
print("Status Code:", response.status_code)
print("Response Body:", response.text)

