distancia = int(input("Digite em quilômetros a distância da viagem: "))
valorGasolina = float(input("Digite o preço da gasolina: "))
autonomia = float(input("Digite a autonomia do veículo: "))

print(f"Custo estimado na viagem: R${(autonomia / distancia) * valorGasolina}")
