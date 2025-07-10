import os, sys

strDir = os.path.dirname(__file__)
try:
   arqLeitura = open(f'{strDir}\\contacao_dolar.csv', 'r', encoding='utf-8')
except FileNotFoundError:
   sys.exit('\nERRO: Arquivo não encontrado...')
except Exception as erro:
   sys.exit(f'\nERRO: {erro}')
else:
    strlista = list()

lstCabecalho = arqLeitura.readline().strip().split(';')
while True:
      strLinha = arqLeitura.readline().strip()   
      if not strLinha: break
      lstAux = [int(i) if i.isdigit() else i for i in strLinha.split(';')]    