n = int(input("Quantos números deseja informar? "))

if (n <= 0):
    print("A quantidade deve ser maior que zero.")
else:
    soma = 0
    menor = 0
    maior = 0

    for i in range(1, n + 1):
        numero = int(input(f"Digite o {i}º número: "))

        soma = soma + numero

        if (i == 1):
            menor = numero
            maior = numero
        else:
            if numero < menor:
                menor = numero
            if numero > maior:
                maior = numero

    print(f"Menor valor: {menor}")
    print(f"Maior valor: {maior}")
    print(f"Soma dos valores: {soma}")
