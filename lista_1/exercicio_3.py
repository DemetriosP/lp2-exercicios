salario = float(input("Informe o sálario do funcionario: "))
aumento = float(input("Informe o percentual de aumento: "))
salario_aumentado = salario * (aumento / 100) + salario

print(f"O valor do aumento é {salario * (aumento / 100)}")
print(f"O novo salário é {salario_aumentado}")
