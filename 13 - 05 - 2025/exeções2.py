from inspect import trace
import sys

try:
    intdivindedo = int(input('digite o divindedo: '))
    intdivisor = int(input('digiter o divisor'))
    fltresultando = intdivindedo / intdivisor
except ValueError:
    print('ERRO: informe um valor que possa ser convetindo em inteiro')
except ZeroDivisionError:
    print('ERRO:nao existe divisão por zero')
except:
    print(f'ERRO: {sys.exc_info()}')  
else:
    print(fltresultando)              






