altura = float(input("Digite a altura (em metros): "))
sexo = input("Digite o sexo (M/F): ")

if(sexo == "M"):
    peso_ideal = (72.7 * altura) - (58)
else:
    peso_ideal = (62.1 * altura) - (44.7)

print(f"Peso ideal: {peso_ideal:.2f} kg")
