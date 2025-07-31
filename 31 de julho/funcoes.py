def mdc(intValorA, intValorB):
    if not isinstance(intValorA, int):
        raise ValueError("\nERRO: O argumento 'intValorA' deve ser do tipo INT")
    if not isinstance(intValorB, int):
        raise ValueError("\nERRO: O argumento 'intValorB' deve ser do tipo INT")

    intAux_A = intValorA
    intAux_B = intValorB

    while intAux_B != 0:
        intAux_A, intAux_B = intAux_B, intAux_A % intAux_B

    print(f'MDC({intValorA}, {intValorB}) = {intAux_A}')
    return intAux_A


def fibonacci(intQtNumeros):
    if not isinstance(intQtNumeros, int):
        raise ValueError("\nERRO: O argumento 'intQtNumeros' deve ser do tipo INT")

    if intQtNumeros <= 0:
        print("A sequência de Fibonacci requer um número inteiro positivo.")
        return []

    sequencia = [0, 1]
    while len(sequencia) < intQtNumeros:
        sequencia.append(sequencia[-1] + sequencia[-2])

    print(f"Fibonacci({intQtNumeros}): {sequencia[:intQtNumeros]}")
    return sequencia[:intQtNumeros]



