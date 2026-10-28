contador = 0

while True:
    numero = int(input("Digite um número (-999 para encerrar): "))

    if (numero == -999):
        break

    if (numero % 2 != 0):
        contador = contador + 1

print(f"Quantidade de números ímpares: {contador}")
