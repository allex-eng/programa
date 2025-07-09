import os,sys

strdir = os.path.dirname(__file__)

try:
    arqleitura = open(f'{strdir}\\times.csv', 'r', encoding='utf-8')
except FileNotFoundError:
    sys.exit('\nerro!: arquivo não existe')
except Exception as erro:
    sys.exit(f'Erro: {erro}')
else:
    lsttimes = []
    while True:
        strlinha = arqleitura.readline().strip()
        if not strlinha:
            break

        lstaux = [int(i) if i.isdigit() else i for i in strlinha.split(';')]
        lsttimes.append(lstaux)
    arqleitura.close()

    for time in lsttimes:
        
        time.insert(4, time[1]*3 + time[2])
     
        time.append(time[5] - time[6])

    
    lsttimes.sort(key=lambda time: (time[4], time[1], time[7], time[5]), reverse=True)

    for time in lsttimes:
        print(time)
