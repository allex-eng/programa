import requests, sys
try:
    reqHTTP = requests.get('https://api.cartola.globo.com/atletas/mercado')
except Exception as e:
    sys.exit(f'erro: {e}')
else:
    if reqHTTP.status_code != 200:
        sys.exit('erro!!!!!!!!!')

dictcartola = reqHTTP.json()
print(dictcartola)
