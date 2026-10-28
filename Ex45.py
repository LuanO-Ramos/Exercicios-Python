ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = int(input("Ano atual: "))

anos = ano_atual - ano_nascimento
meses = anos * 12
dias = anos * 365
semanas = dias // 7

print(f"Idade em anos: {anos}")
print(f"Idade em meses: {meses}")
print(f"Idade em dias: {dias}")
print(f"Idade em semanas: {semanas}")
