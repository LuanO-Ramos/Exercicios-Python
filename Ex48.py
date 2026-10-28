preco = float(input("Preço de etiqueta: R$ "))
print("Condições de pagamento:")
print("1 - À vista em dinheiro ou pix (10% de desconto)")
print("2 - À vista no cartão de crédito (5% de desconto)")
print("3 - Em duas vezes (preço normal)")
print("4 - Em três vezes (10% de juros)")
codigo = int(input("Escolha o código: "))

if codigo == 1:
    valor_final = preco * 0.90
elif codigo == 2:
    valor_final = preco * 0.95
elif codigo == 3:
    valor_final = preco
elif codigo == 4:
    valor_final = preco * 1.10
else:
    valor_final = None

if valor_final is None:
    print("Código inválido!")
else:
    print(f"Valor a pagar: R$ {valor_final:.2f}")
