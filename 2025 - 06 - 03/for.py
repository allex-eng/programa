import sys

numero = None

try:
    numero = int(input('Digite um numero para calcular se é primo: '))
except ValueError: 
    sys.exit('ERRO: Digite um número inteiro positivo.')
except Exception as e:
    sys.exit(f'ERRO: {e}')
else:
    contDivisor = 0
    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            contDivisor += 1

    if contDivisor == 2:
        print(f'{numero} é primo.')
    else:
        print(f'{numero} não é primo.')