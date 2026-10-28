menor = 0
maior = 0

for i in range(1, 21):
    numero = int(input(f"Digite o {i}º número: "))

    if (i == 1):
        menor = numero
        maior = numero
    else:
        if (numero < menor):
            menor = numero
        if (numero > maior):
            maior = numero

print(f"Menor número: {menor}")
print(f"Maior número: {maior}")
