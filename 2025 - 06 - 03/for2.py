import sys

numero = None

try:
    numero = int(input('Digite um numero para calcular seu fatorial: '))
except ValueError: 
    sys.exit('ERRO: Digite um número inteiro positivo')
except Exception as e:
    sys.exit(f'ERRO: {e}')
else:
    if numero < 0:
        print('Não existe fatorial.')
    elif numero < 2:
        print(f'Fatorial de {numero} = 1')
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        print(f'Fatorial de {numero} = {resultado}')