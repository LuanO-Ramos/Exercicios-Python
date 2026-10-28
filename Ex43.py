qtd_moedas1 = int(input("Moedas de 1 centavo: "))
qtd_moedas5 = int(input("Moedas de 5 centavos: "))
qtd_moedas10 = int(input("Moedas de 10 centavos: "))
qtd_moedas25 = int(input("Moedas de 25 centavos: "))
qtd_moedas50 = int(input("Moedas de 50 centavos: "))
qtd_moedas100 = int(input("Moedas de 1 real: "))

total = qtd_moedas1 * 0.01 + qtd_moedas5 * 0.05 + qtd_moedas10 * 0.10 + qtd_moedas25 * 0.25 + qtd_moedas50 * 0.50 + qtd_moedas100 * 1.00

print(f"Total economizado: R$ {total:.2f}")
