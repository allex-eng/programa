try:
    multiplicando = int(input("Digite o multiplicando: "))
    multiplicador = int(input("Digite o multiplicador: "))

    if multiplicando < 0 or multiplicador < 0:
        print("Por favor, digite apenas números inteiros positivos.")
    else:
        resultado = 0
        contador = 0

        while contador < multiplicador:
            resultado += multiplicando
            contador += 1

        print(f"{multiplicando} x {multiplicador} = {resultado}")

except ValueError:
    print("Entrada inválida! Por favor, digite apenas números inteiros.")