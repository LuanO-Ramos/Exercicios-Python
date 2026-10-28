cotacao = float(input("Cotação do dólar (R$): "))
dolar = float(input("Valor em dólar (US$): "))

real = dolar * cotacao

print(f"US$ {dolar:.2f} equivalem a R$ {real:.2f}")
