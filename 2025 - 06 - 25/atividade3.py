import sys, random


try:
    intN = int(input("Informe o valor de N (1 a 100): "))
    if intN < 1 or intN > 100:
        sys.exit("\nERRO: informe um valor inteiro entre 1 e 100.")
except ValueError:
    sys.exit("\nERRO: informe um valor inteiro válido…")
except Exception as erro:
    sys.exit(f"\nERRO inesperado: {erro}…")


lista = [random.randint(-100, 100) for _ in range(intN)]

print("\nLista original:")
print(lista)


print("\nSublistas (anterior, atual, próximo):")
for i in range(intN):
    anterior = lista[i - 1] if i > 0 else lista[i]
    atual = lista[i]
    proximo = lista[i + 1] if i < intN - 1 else lista[i]
    print([anterior, atual, proximo])
