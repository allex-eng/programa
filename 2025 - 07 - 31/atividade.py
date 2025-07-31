from seu_modulo import mediaIFRN_v1, mediaIFRN_v2, mediaIFRN_v3

def obter_nota(nome):
    while True:
        try:
            nota = int(input(f"Digite a {nome} (0 a 100): "))
            if 0 <= nota <= 100:
                return nota
            else:
                print("Nota deve estar entre 0 e 100.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

nota1 = obter_nota("primeira nota")
nota2 = obter_nota("segunda nota")

# Escolha a função desejada
media = mediaIFRN_v1(nota1, nota2)
print(f"Média calculada: {media}")
