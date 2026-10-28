print("===== CARDÁPIO =====")
print("1 - Bife acebolado   R$ 15,00")
print("2 - Lasanha          R$ 25,00")
print("3 - Frango grelhado  R$ 18,00")
print("4 - Feijoada         R$ 30,00")
print("5 - Strogonoff       R$ 22,00")
print("6 - Peixe frito      R$ 28,00")

opcao = int(input("Escolha o prato (1 a 6): "))

if (opcao == 1):
    prato = "Bife acebolado"
    preco = 15.00
elif (opcao == 2):
    prato = "Lasanha"
    preco = 25.00
elif (opcao == 3):
    prato = "Frango grelhado"
    preco = 18.00
elif (opcao == 4):
    prato = "Feijoada"
    preco = 30.00
elif (opcao == 5):
    prato = "Strogonoff"
    preco = 22.00
elif (opcao == 6):
    prato = "Peixe frito"
    preco = 28.00
else:
    prato = ""
    preco = 0

if (preco == 0):
    print("Opção inválida!")
else:
    print(f"Você escolheu: {prato} (R$ {preco:.2f})")
    resposta = input("Aceita pagar a gorjeta do garçom 10% sobre o valor do prato? (S/N): ")

    if (resposta == "S" or resposta == "s"):
        valor_final = preco * 1.10
    else:
        valor_final = preco

    print(f"Valor final: R$ {valor_final:.2f}")
