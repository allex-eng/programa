# solicite numeros inteiros e positivos aleatoriamente ate que seja informando o valor 0
# quando for digitar o valor 0:

# 1) quantos numeros inteiros foram digitados;
# 2)a soma dos numeros inteiros positivos;
# 3) a media dos numeros inteiros positivos;
# 0 não dever considerado em nenhum dos item 

valor = None
soma = 0
qtvalor = 0
qtsoma = 0
from logging import exception
import sys
while valor != 0:
    try:
        valor = int(input('digite um valor'))
    exception ValueError:
        print('so valores corretos')   
