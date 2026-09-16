qtd_frangos = int(input("Digite a quantidade de frangos: "))

preco_anel_chip = 4.00
preco_anel_alimento = 3.50

gasto_por_frango = (preco_anel_chip) + (2 * preco_anel_alimento)

gasto_total = (qtd_frangos * gasto_por_frango)

print(f"Gasto por frango: R$ {gasto_por_frango:.2f}")
print(f"Gasto total da granja: R$ {gasto_total:.2f}")
