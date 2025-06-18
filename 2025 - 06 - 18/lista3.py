lisnome = list()

while True:
    nome = input('Digite um nome: ').strip()
    if nome.lower() == 'fim':
        break

    if len(nome) > 0:
        lisnome.append(nome)
lisnome.sort(reverse=True)
print(lisnome)

print(lisnome)
