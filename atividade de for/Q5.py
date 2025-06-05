a1 = int(input('digite o valor do primeiro termo:'))
r = int(input('digite o valor da razão:'))
n = int(input('digite o valor dos :'))
if r == 0:
    print('a p.a é constante')
elif r > 0:
     print('a p.a é crescente')
else:
     print('a p.a é descrescente')

for i in range(1, n+1):
    termo = a1 + (i - 1) * r
    if i == n:
        print(f"O {n}º termo da P.A. é {termo}")

