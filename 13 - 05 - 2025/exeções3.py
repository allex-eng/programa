from inspect import trace
import sys
from tkinter import EXCEPTION

try:
    intdivindedo = int(input('digite o divindedo:'))
    intdivisor = int(input('digiter o divisor'))
    fltresultando = intdivindedo / intdivisor
except Exception as tipoexceção:
    print(f'ERRO: {tipoexceção}')   
    print(f'ERRO : {sys.exc_info()}')
else:
    print(fltresultando)







