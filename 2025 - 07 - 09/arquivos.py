import os,sys

strdir = os.path.dirname(__file__)

try:
  arqleitura = open(f'{strdir}\\ times.csv', 'r', encoding='utf-8')
except FileNotFoundError:
    sys.exit('\nerro!: arquivo não existe')

except Exception as erro:
    sys.exit(f'Erro: {erro}')

else:
    lsttimes = list()    
    while True:
        strlinha = arqleitura.readline().strip()

        if not strlinha: break

        
        lstaux = [int(i) if i.isdigit() else i for i in strlinha.split(';')]

        lsttimes.append(lstaux)

        arqleitura.close()

        print(lsttimes)

    





       