Salario_Colaborador = float(input("Digite o salario do colaborador: "))

if(Salario_Colaborador <= 280):
    novo_salario = Salario_Colaborador + (Salario_Colaborador * 0.2)
    print(f"O salário antes do reajuste é de R${Salario_Colaborador:.2f}")
    print("O percentual de aumento aplicado foi de 20%")
    print(f"O valor de aumento foi de {Salario_Colaborador * 0.2:.2f}")
    print(f"O novo salário do colaborador é de R${novo_salario:.2f}")

elif(Salario_Colaborador <= 700):
    novo_salario = Salario_Colaborador + (Salario_Colaborador * 0.15)
    print(f"O salário antes do reajuste é de R${Salario_Colaborador:.2f}")
    print("O percentual de aumento aplicado foi de 15%")
    print(f"O valor de aumento foi de {Salario_Colaborador * 0.15:.2f}")
    print(f"O novo salário do colaborador é de R${novo_salario:.2f}")

elif(Salario_Colaborador <= 1500):
    novo_salario = Salario_Colaborador + (Salario_Colaborador * 0.1)
    print(f"O salário antes do reajuste é de R${Salario_Colaborador:.2f}")
    print("O percentual de aumento aplicado foi de 10%")
    print(f"O valor de aumento foi de {Salario_Colaborador * 0.1:.2f}")
    print(f"O novo salário do colaborador é de R${novo_salario:.2f}")

elif(Salario_Colaborador > 1500):
    novo_salario = Salario_Colaborador + (Salario_Colaborador * 0.05)
    print(f"O salário antes do reajuste é de R${Salario_Colaborador:.2f}")
    print("O percentual de aumento aplicado foi de 5%")
    print(f"O valor de aumento foi de {Salario_Colaborador * 0.05:.2f}")
    print(f"O novo salário do colaborador é de R${novo_salario:.2f}")