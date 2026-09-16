preco = float(input("Digite o preço: "))

desconto = (preco * 0.10)

novo_preco = (preco - desconto)

print(f"Desconto: R$ {desconto:.2f}")
print(f"Novo preço: R$ {novo_preco:.2f}")
