valor_aquisicao = float(input("Digite o valor de aquisição: "))

if(valor_aquisicao < 50.00):
    valor_venda = (valor_aquisicao * 1.45)
else:
    valor_venda = (valor_aquisicao * 1.30)
    
print(f"Valor de venda: R$ {valor_venda:.2f}")
