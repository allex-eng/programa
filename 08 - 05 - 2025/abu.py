'''
 programa para classificar um triângulo quanto aoa ângulos.

-programa deverá solicitar 3 ângulos inteiros positivos;
- para ser um triângunlos, a soma dos ãngulos deve ser igual a 180;

retãngulos: possui um ângulos internos reto (igual a 90)
obtusãngulo: possui um ângulo interno obtuso (maior do que 90)
Acutângulo: possui todos os angulos internos agudos (menores que 90)
'''
import sys

cat_a = input('qual o angulo do cateto adjacente')
if cat_a < 0 or cat_a > 100:
    sys.exit('pegadinha')
cat_o = input('qual o angulo do cateto oposto')
if cat_o < 0 or cat_o > 100:
    sys.exit(' pergadinha')

hip = input('informe o valor da hipotenusa')  
if hip < 0 or hip > 100:
    sys.exit('eraddo')  

trian = cat_a + cat_o + hip
