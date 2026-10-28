a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if (a < b):
    menor = a
    maior = b
else:
    menor = b
    maior = a

print(f"Números entre {menor} e {maior}:")

for i in range(menor + 1, maior):
    print(i)
