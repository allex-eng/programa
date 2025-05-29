import sys

try:
    numero = int(input('Digite um valor: '))
except ValueError:
    sys.exit('ERRO: Valor inválido, digite um número positivo.')
except Exception as e:
    sys.exit(f'ERRO: {e}')

if numero <= 0:
    sys.exit('ERRO: Digite um valor positivo.')

else:
    div = 1
    div2 = 2
while div2 <= numero:
    if numero % div2 ==0:
        div += 1
        



