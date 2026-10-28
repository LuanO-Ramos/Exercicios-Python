populacao_a = 80000
populacao_b = 200000
anos = 0

while pop_a < pop_b:
    populacao_a = populacao_a * 1.03
    populacao_b = populacao_b * 1.015
    anos = anos + 1

print(f"Anos necessários: {anos}")
print(f"População de A: {pop_a:.0f}")
print(f"População de B: {pop_b:.0f}")
