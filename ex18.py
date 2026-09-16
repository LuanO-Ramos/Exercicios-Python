valor_hora = float(input("Qual o valor da hora trabalhada: "))
qta_horas_mes  = float(input("Quantidade de horas trabalhadas no mês: "))

salario_bruto  = valor_hora*qnt_hors_mes

if(salario_bruto <=900):
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    total_desconto = inss
    salario_liquido = salario_bruto - total_desconto
    print(f"(-) IR ISENTO")
    print(f"(-) INSS {inss}")
    print(f" FGTS {inss}")
    print(f" Total de Descontos R${total_desconto}")
    print(f" Salário Líquido R${salario_liquido}")


elif(salario_bruto <=1500):
    ir = salario_bruto * 0.05
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    total_desconto = inss + ir
    salario_liquido = salario_bruto - total_desconto
    print(f"(-) IR {ir}")
    print(f"(-) INSS {inss}")
    print(f" FGTS {inss}")
    print(f" Total de Descontos R${total_desconto}")
    print(f" Salário Líquido R${salario_liquido}")


elif(salario_bruto <=2500):
    ir = salario_bruto * 0.2
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    total_desconto = inss + ir
    salario_liquido = salario_bruto - total_desconto
    print(f"(-) IR {ir}")
    print(f"(-) INSS {inss}")
    print(f" FGTS {inss}")
    print(f" Total de Descontos R${total_desconto}")
    print(f" Salário Líquido R${salario_liquido}")