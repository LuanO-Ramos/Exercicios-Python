total = float(input("Valor total da conta: R$ "))

parte_inteira = int(total // 3)
willian = total - 2 * parte_inteira

print(f"Maria: R$ {parte_inteira:.2f}")
print(f"Gabriel: R$ {parte_inteira:.2f}")
print(f"Willian: R$ {willian:.2f}")
