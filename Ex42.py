latas = int(input("Quantidade de latas de 350 ml: "))
garrafas_600 = int(input("Quantidade de garrafas de 600 ml: "))
garrafas_2l = int(input("Quantidade de garrafas de 2 litros: "))

litros = latas * 0.35 + garrafas_600 * 0.6 + garrafas_2l * 2

print(f"Total comprado: {litros:.2f} litros")
