numero = int(input("Digite um número inteiro de 1 a 10: "))

if (numero >= 1 and numero <= 10):
    print(f"Tabuada de {numero}:")
    for i in range(1, 11):
        print(f"{numero} X {i} = {numero * i}")
else:
    print("Número inválido")
