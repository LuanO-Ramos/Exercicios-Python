qtd_sanduiches = int(input("Digite a quantidade de sanduíches: "))

peso_queijo = (2 * 50)    
peso_presunto = (1 * 50)
peso_carne = (1 * 100)    

total_queijo_g = (qtd_sanduiches * peso_queijo)
total_presunto_g = (qtd_sanduiches * peso_presunto)
total_carne_g = (qtd_sanduiches * peso_carne)

total_queijo_kg = (total_queijo_g / 1000)
total_presunto_kg = (total_presunto_g / 1000)
total_carne_kg = (total_carne_g / 1000)

print(f"Queijo necessário: {total_queijo_kg:.2f} kg")
print(f"Presunto necessário: {total_presunto_kg:.2f} kg")
print(f"Carne necessária: {total_carne_kg:.2f} kg")
