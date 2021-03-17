salario = float(input("Informe o salario: "))
cheque_1 = float(input("Informe o valor do primeiro cheque: "))
cheque_2 = float(input("Informe o valor do segundo cheque: "))

descontos = (cheque_1 + (cheque_1 * 0.0038)) + (cheque_2 + (cheque_2 * 0.0038))
saldo = salario - descontos

print(f"Seu saldo é de {round(saldo)} reais")
