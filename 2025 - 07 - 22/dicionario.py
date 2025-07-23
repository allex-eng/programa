
from logging import exception
import os,sys,json

dir_app = os.path.dirname(__file__)

strnomearq = f'{dir_app}//cartola_fc_2024.json'
try:
    arqinput = open(strnomearq, 'r' , encoding='utf-8')
    strdados = arqinput.read()
    dictcartola = json.loads(strdados)
    arqinput.close()
except FileNotFoundError:
    sys.exit('erro: n existe arquivo')
except json.JSONDecodeError:
    sys.exit('erro: arquivo n estao no formanto correto')
except exception as erro:
    sys.exit(f'{erro}')
else:
     lstchaves =list(dictcartola.key())

strclube = input('informe:').strip().lower()




