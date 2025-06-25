import sys, random  

try:
    intN = int(input('Informe o valor de N (1 a 100): '))
    if intN < 1 or intN > 100:
        sys.exit('\nERRO: informe um valor inteiro entre 1 e 100.')
except ValueError:
    sys.exit('\nERRO: informe um valor inteiro válido...')
except Exception as erro:
    sys.exit(f'\nERRO inesperado: {erro}...')


lista_aleatoria = random.sample(range(0, 1001), intN)
print('Lista gerada:', lista_aleatoria)


lista_raizes = [num ** 0.5 for num in lista_aleatoria]  
print('Lista de raízes quadradas:', lista_raizes)
