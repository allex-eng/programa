# calcular media da disciplina do ifrn
#
# 1) solicitar ao usuário que infome duas notas (AS notas são inteiras)
# 2) calcular a média IFRN
# 3) Exibir a média sem casa decimal

ETAP1 = float(input("digite o valor da primeira etapa"))

ETAP2 = float(input("digite o valor da segumda etapa"))

media = (ETAP1 * 2 + ETAP2 * 3) / 5

print(f"A media é: {media:.0f}")
