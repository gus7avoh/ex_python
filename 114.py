import requests

url = 'https://pudim.com.br'

try: 
    response = requests.get(url)
   
    response.raise_for_status()  
    print('Acesso bem-sucedido!')

except :
    print('Erro ao acessar o site:')




#, e requests.exceptions.RequestException as e