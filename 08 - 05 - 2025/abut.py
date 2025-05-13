'''
 programa para classificar um triângulo quanto aoa ângulos.

-programa deverá solicitar 3 ângulos inteiros positivos;
- para ser um triângunlos, a soma dos ãngulos deve ser igual a 180;

retãngulos: possui um ângulos internos reto (igual a 90)
obtusãngulo: possui um ângulo interno obtuso (maior do que 90)
Acutângulo: possui todos os angulos internos agudos (menores que 90)
'''
import sys

angA = int(input('digite o angulo A:'))
angB = int(input('digite o angulo B: '))
angC = int(input('digite o angulo C: '))
if (angA <= 0) or (angB <= 0) or (angC <= 0):
    sys.exit('ERRO:')