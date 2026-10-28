codigo = []
veiculos = []
acidentes = []
indices = []

for i in range(5):
  print(f"\nCidade {i+1}:")

  codigo_cidade = int(input("Código da cidade: "))
  qtd_veiculos = int(input("Número de veículos: "))
  qtd_acidentes = int(input("Números de acidentes com vítimas: "))

  codigo.append(codigo_cidade)
  veiculos.append(qtd_veiculos)
  acidentes.append(qtd_acidentes)

  if (qtd_veiculos > 0):
    indice_acidentes = qtd_acidentes / qts_veiculos * 100
  else:
    indice_veiculos = 0

  indices.append(indice_acidentes)

maior = max(indices)
menor = min(indices)

posicao_maior = indices.index(maior)
posicao_menor = indices.index(menor)

print(f"O maior índice de acidentes é de {maior}, o código da cidade que pertence é {codigo[posicao_maior]}")
print(f"O menor índice de acidentes é de {menor}, o código da cidade que pertence é {codigo[posicao_menor]}")

media_veiculos = sum(veiculos) / 5
print(f"A média de veículos nas 5 cidades foram de {media_veículos}")

soma_acidentes = 0
quantidade_cidades = 0

for i in range(5):
  if (veiculos[i] < 2000):
    soma_acidentes += acidentes[i]
    quantidade_cidades += 1

  if (quantidade_cidades > 0):
    media_acidentes = soma_acidentes / quantidade_cidades
    print(f"Média de acidentes nas cidades com menos de 2000 veículos é de {media_acidentes}")
  else:
    print(f"Nenhuma cidade possui menos de 2000 veículos.")



  
