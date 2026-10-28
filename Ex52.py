contador = 0

numero = int(input("Digite um número (-1 para encerrar): "))

while numero != -1:
    contador = contador + 1
    numero = int(input("Digite um número (-1 para encerrar): "))

print(f"Quantidade de números digitados: {contador}")
