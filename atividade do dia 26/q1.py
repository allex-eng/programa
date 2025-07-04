'''
   Dada a lista lstNomes (no início do código), faça um programa que:
   
      1) Gere mais duas listas (lstNotas_1 e lstNotas_2), cada uma com N notas aleatórias
         entre 0 e 100 (inclsuive). Cada uma dessas listas deverá ter exatamente notas
         para cada um dos nomes em lstNomes;

      2) Gere uma lista (lstBoletins), onde cada posição será uma sub-lista contendo um dos
         dos nomes de lstNomes e suas respectivas notas (lstNotas_1 e lstNotas_2);

      3) Após lstBoletins ser gerada, adicione em cada posição mais duas informações:

         a) A média das notas (utilize como referência o cálculo de média do IFRN);

         b) A situação do aluno (Aprovado, Prova Final ou Reprovado) seguindo os 
            critérios do IFRN;

         c) Liste todos os boletins.

      4) Ordene os Boletins (lstBoletins) em ordem decrescente de média e em seguida liste-os;

      5) Filtre e liste apenas os alunos aprovados;
'''

lstNomes = ['Scooby-Doo'       , 'Fred Flintstone', 'Zé Colmeia' , 'Dom Pixote'     , 
            'Muttley'          , 'Bionicão'       , 'Tutubarão'  , 'Capitão Caverna', 
            'Formiga Atômica'  , 'Jonny Quest'    , 'Space Ghost', 'Manda-Chuva'    , 
            'Barney Rubble'    , 'Salsicha'       , 'Falcão Azul', 'Batatinha'      , 
            'Penélope Charmosa', 'Pepe Legal'     , 'Catatau'    , 'Dick Vigarista' ]

# ----------------------------------------------------------------------
# Questão 01
import sys
import random

try:
    intN = int(input('Informe o valor de N (número de notas por nome): '))
    if intN <= 0:
        sys.exit('Valor inválido: o número deve estar entre 0 e 20.')
except ValueError:
    sys.exit('\nERRO: informe um valor inteiro válido...')
except Exception as erro:
    sys.exit(f'\nERRO inesperado: {erro}...')

lstNotas_1 = [[random.randint(0, 100) for _ in range(intN)] for _ in lstNomes]
lstNotas_2 = [[random.randint(0, 100) for _ in range(intN)] for _ in lstNomes]

print("\nNotas dos Alunos:")
for i in range(len(lstNomes)):
    print(f"{lstNomes[i]:<20} | Notas 1: {lstNotas_1[i]} | Notas 2: {lstNotas_2[i]}")


# ----------------------------------------------------------------------
# Questão 02
lstBoletins = [[lstNomes[i], lstNotas_1[i], lstNotas_2[i]] for i in range(len(lstNomes))]

# ----------------------------------------------------------------------
# Questão 03
lstBoletins = [
    boletim + [
        round(((sum(boletim[1]) / len(boletim[1]) + sum(boletim[2]) / len(boletim[2])) / 2), 2),
        "Aprovado" if ((sum(boletim[1]) / len(boletim[1]) + sum(boletim[2]) / len(boletim[2])) / 2) >= 60
        else "Prova Final" if ((sum(boletim[1]) / len(boletim[1]) + sum(boletim[2]) / len(boletim[2])) / 2) >= 30
        else "Reprovado"
    ]
    for boletim in lstBoletins
]

print("\nBoletins (compreensão de lista):")
for b in lstBoletins:
    print(f"{b[0]:<20} | Média: {b[3]:5.2f} | Situação: {b[4]}")



# ----------------------------------------------------------------------
# Questão 04
# TODO: Fazer na sala de aula no dia 01/07/2026
# TODO: Pesquisar a função SORT() usando funções LAMBDA


# ----------------------------------------------------------------------
# Questão 04
# TODO: Fazer na sala de aula no dia 01/07/2026
# TODO: Pesquisar a função FILTER() usando funções LAMBDA