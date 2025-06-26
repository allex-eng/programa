import sys, random


try:
    intN = int(input("Informe o valor de N (1 a 100): "))
    if intN < 1 or intN > 100:
        sys.exit("\nERRO: informe um valor inteiro entre 1 e 100.")
except ValueError:
    sys.exit("\nERRO: informe um valor inteiro válido…")
except Exception as erro:
    sys.exit(f"\nERRO inesperado: {erro}…")

livalores = list()

for _ in range(intN):
    intvalor = random.randint(-100,100)
    
    list