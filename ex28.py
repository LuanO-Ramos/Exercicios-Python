primeiro_int = int(input("Digite o primeiro número inteiro: "))
segundo_int = int(input("Digite o segundo número inteiro: "))
primeiro_real = float(input("Digite número real: "))

produto  = (primeiro_int * 2) * (segundo_int / 2)
soma = (primeiro_int * 3) + (primeiro_real)
ao_cubo = (primeiro_real ** 3)

print(f"Produto do dobro do primeiro com a metade do segundo: {produto}")
print(f"Soma do triplo do primeiro com o terceiro: {soma}")
print(f"Terceiro elevado ao cubo: {ao_cubo}")
