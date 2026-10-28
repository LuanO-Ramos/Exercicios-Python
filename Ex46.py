nome = input("Nome: ")
sexo = input("Sexo (M/F): ").upper()
estado_civil = input("Estado civil: ").upper()

if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Tempo de casada (anos): "))
    print(f"{nome} é casada há {tempo_casada} anos.")
