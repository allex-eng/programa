'''
 programa para classificar um triângulo quanto aoa ângulos.

-programa deverá solicitar 3 ângulos inteiros positivos;
- para ser um triângunlos, a soma dos ãngulos deve ser igual a 180;

retãngulos: possui um ângulos internos reto (igual a 90)
obtusãngulo: possui um ângulo interno obtuso (maior do que 90)
Acutângulo: possui todos os angulos internos agudos (menores que 90)
'''
n = int(input('digite o valor: '))
soma = 1
x = 1
while x <= n:
    soma = soma + x
    x = x + 1 
    print(f'o resultando é,{soma}')