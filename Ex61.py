numero = int(input("Digite um número inteiro: "))

if (numero < 0):
    print("Fatorial não existe para números negativos.")
else:
    fatorial = 1

    for i in range(1, numero + 1):
        fatorial = fatorial * i

    print(f"{numero}! = {fatorial}")
