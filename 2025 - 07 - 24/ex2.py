import requests, sys
try:
    reqHTTP = requests.get('https://viacep.com.br/ws/59143030/json')
except Exception as e:
    sys.exit(f'erro: {e}')
else:
    if reqHTTP.status_code != 200:
        sys.exit('erro!!!!!!!!!')

dictcartola = reqHTTP.json()
print(dictcartola)
