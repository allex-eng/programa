import os

strdir = os.path.dirname(__file__) 
try:
    argleitura = open(f'{str}\\carta.txt', 'r ', encoding = 'utf-8')
    strconteudo = argleitura.readlines()
    argleitura.close()
    print(strconteudo)

except FileNotFoundError:
    print('ERRO: arquivo não existe')


except Exception as erro:
    print(f'Erro: {erro}')
else:
    strconteudo = argleitura.readline()
    argleitura.close()
    print(strconteudo)
  
while True:
    strconteudo = argleitura.readline()
    if not strconteudo:
        break
    print('-' * 80)
    print(strconteudo).strip()

