import os

strdir = os.path.dirname(__file__)

try:
    with open(f'{strdir}\\carta.txt', 'r', encoding='utf-8') as argleitura:
        strconteudo = argleitura.readlines()
        print(strconteudo)

        print('-' * 80)
        for linha in strconteudo:
            print(linha.strip())

except FileNotFoundError:
    print('ERRO: arquivo não existe')

except Exception as erro:
    print(f'Erro: {erro}')


