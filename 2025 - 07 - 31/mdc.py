def gcd_iterativo(a, b):
    
    while(b):
        a, b = b, a % b
    return a

def gcd_recursivo(a, b):  
   
    if b == 0:
        return a
    else:
        return gcd_recursivo(b, a % b)


num1 = int(input('digite:'))
num2 = int(input('digite:'))
print(f"O MDC de {num1} e {num2} é: {gcd_iterativo(num1, num2)}")
