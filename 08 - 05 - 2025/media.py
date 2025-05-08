# programa para calcular a média de uma disciplina semesntral no ifrn
# as notas dever ser inteiras e entre 0 e 100 (inclusive)

#caso media seja igual ou superior a 60 o aluno estará aprovado;
#casoa média sejam ou superior a 20 o aluno estara em prova final e os demais casos estará reprovado

import sys

etapa1 = int(input('informer a nota da etapa 1: '))
if etapa1 < 0 or etapa1 > 100:
    sys.exit('ERRO: nota 1 inválida. informer nota entre 0 e 100.')

etapa2 = int(input('informe a nota da etapa 2: '))
if etapa2 < 0 or etapa2  > 100:
    sys.exit('ERRO: nota 2 inválida. informer nota entra 0 e 100.')

media = (etapa1 * 2 + etapa2 * 3) / 5
print(f'media do aluno:{media:.0f}')  

if media >= 60:
    print('aluno aprovado.')
elif media >=20:
    print ('aluno ira fazer prova final')  
else:
    print('Aluno reprovado,que feio em.')     

