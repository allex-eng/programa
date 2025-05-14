# Solicita o número ao usuário
numero = input("Digite um número inteiro positivo de até 4 dígitos: ")

# Verifica se a entrada é válida
if numero.isdigit() and 1 <= len(numero) <= 4:
    # Converte cada caractere para inteiro e soma
    soma = sum(int(digito) for digito in numero)
    print(f"A soma dos algarismos de {numero} é: {soma}")
else:
    print("Entrada inválida! Certifique-se de digitar um número inteiro positivo com até 4 dígitos.")
