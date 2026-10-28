livros = int(input("Quantidade de livros comprados no bimestre: "))

if (livros == 0):
    pontos = 0
elif (livros == 1):
    pontos = 5
elif (livros == 2):
    pontos = 15
elif (livros == 3):
    pontos = 30
else:
    pontos = 60

print(f"Pontos: {pontos}")

if (pontos >= 65):
    print("Escolha entre: 2 livros (valor máximo de R$ 100,00) OU Power bank")
elif (pontos >= 35 and pontos <= 60):
    print("Escolha entre: Um livro (valor máximo de R$ 30,00) OU Luminária de cabeceira")
elif (pontos >= 20 and pontos <= 30):
    print("Escolha entre: Uma Eco Bag OU Caneta personalizada")
else:
    print("Pontos insuficientes para receber um brinde")
