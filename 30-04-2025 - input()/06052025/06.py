# EM um movimento retilíneo uniformemte variado (MRU), a fórmula para calcular a distância percorrida é dada por:
import sys
velo = int(input("informer a velocidade 1"))
if velo <=0:
    sys.exit('informe uma velocida positiva')

tempo = int(input("informer o tempo"))

acel = int(input("informer a acaleraçao"))

delta = velo * tempo + (acel * (tempo * tempo)) / 2


print(f"o resultando de delta é {delta} ")h



