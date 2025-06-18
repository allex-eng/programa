from logging import exception


lstaluno = list()
nota1 = list()
nota2 = list()

while True:
    nome = input('Digite um nome: ').strip()
    if nome.lower() == 'fim':
        break

    try:
        nota1 = int(input('valor 1:'))
        nota2 = int(input('valor2: '))
        except ValueError:
            print('erroooo')
        except exception as e:
            print(f'errou{e}')
        else:
            if nota1 < 0 or nota1 > 100:
                print('erro')    
            elif nota2    