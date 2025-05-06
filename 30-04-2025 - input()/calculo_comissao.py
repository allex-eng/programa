valor_venda = float(input('digite o valor da venda (R$)' ))
percentual = float(input('informe a comissão (%)......: ' ))

comissao = valor_venda * percentual / 100

print(f'o valor da comissão é R$ {comissao:.2f}')