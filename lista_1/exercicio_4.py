salario = float(input("Informe o salário do funcionario: "))
gratificacao = salario * 0.05
imposto = salario * 0.07

salario_receber = salario + gratificacao - imposto

print(f"O salário a receber é {salario_receber}")
