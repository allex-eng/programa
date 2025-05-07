import sys
distancia = int(input(' digiter a distancia (km)'))
if distancia <=0:
    sys.exit('informe distancia positiva')

v_ini = int(input('digiter a velocida (km/h)'))
if v_ini <=0:
    sys.exit('informe velocidade positiva')

acelera = int(input('digiter a aceleração (m/s²)'))  
if acelera <=0:
    sys.exit('informe aceleração positivo')

distancia *= 100  
v_ini /= 3.6

delta = v_ini ** 2 - 4 * acelera * distancia
if delta <0:
    sys.exit(' não é possivel calcular o delta')

t=(-v_ini + distancia ** 0.5) / (2 * acelera)  

hora = t // 3600
t = t % 3600
minuto = t // 60
segundo = t % 60

print(f'tempo = {hora}:{minuto}:{segundo}')


