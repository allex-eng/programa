import sys

try:
    intMultiplicador = int(input('Digite o Multiplicador: '))
    intMultiplicando = int(input('Digite o Multiplicando: '))
except ValueError:
    sys.exit('ERRO: Não foi informado um valor inteiro válido...')
except Exception as e:
    sys.exit(f'ERRO: {e}')
else:
    if intMultiplicador <= 0:
        sys.exit('ERRO: Informe Multiplicador Positivo...')

    if intMultiplicando <= 0:
        sys.exit('ERRO: Informe Multiplicando Positivo...')

    intProduto = 0
    for _ in range(intMultiplicador):
        intProduto += intMultiplicando

    print(f'{intMultiplicador} x {intMultiplicando} = {intProduto}')
