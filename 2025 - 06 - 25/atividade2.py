import sys, random, math

try:
    intN = int(input('Informe o valor de N (1 a 100): '))
    if intN < 1 or intN > 100:
        sys.exit('\nERRO: informe um valor inteiro entre 1 e 100.')
except ValueError:
    sys.exit('\nERRO: informe um valor inteiro válido...')
except Exception as erro:
    sys.exit(f'\nERRO inesperado: {erro}...')

listavalores = list()

intcontaodr = 1
while intcontaodr <= intN:
    intvalor = random.randint(0,1000)
    
    if intvalor not in listavalores:
        listavalores.append(intvalor)
        intcontaodr += 1
            
print(listavalores)   

for intvalor in listavalores:
    raiz = math.sqrt(intvalor) 
    print(f'Valor: {intvalor} - Raiz quadrada: {raiz:.2f}')
