#import Plano_Contratacao 
import InserirAta

"""
response = Plano_Contratacao.InserirPlanoContratacao()
print("Status Code:", response.status_code)
print("Response Body:", response.text)

"""

response = InserirAta.InserirAta(2030, 1)
print("Status Code:", response.status_code)
print("Response Body:", response.text)

