contador = 0

while True:
    numero = int(input("Digite um número (0 para encerrar): "))

    if (numero == 0):
        break

    if (numero == 50):
        contador = contador + 1

print(f"O número 50 foi informado {contador} vez")
