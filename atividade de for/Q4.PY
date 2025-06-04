
n = int(input('Digite o número de termos : '))
a1 = float(input('Digite o primeiro termo : '))
q = float(input('Digite a razão (q): '))


for i in range(n):
    termo = a1 * q ** i
    print(f'Termo {i + 1}: {termo}')
