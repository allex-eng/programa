import sys, random

try:
    intN = int(input('Informe o valor de N (1 a 100): '))
    if intN < 1 or intN > 100:
        sys.exit('\nERRO: informe um valor inteiro entre 1 e 100.')
except ValueError:
    sys.exit('\nERRO: informe um valor inteiro válido...')
except Exception as erro:
    sys.exit(f'\nERRO inesperado: {erro}...')      

else:
    lista_aleatoria = [random.randint(0, 1000) for _ in range(intN)]
    print('Lista gerada:', lista_aleatoria)  

lista_qua = [num for num in lista_aleatoria if num **2]
print('as raizes da lista anterior', lista_qua)

      