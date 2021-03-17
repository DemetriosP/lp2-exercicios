horas_trabalhadas = float(input("Informe o numero de horas trabalhadas: "))
salario_minimo = float(input("Informe o salario minimo: "))
valor_hora_trabalhada = (salario_minimo / 2)
salario_bruto = horas_trabalhadas * valor_hora_trabalhada
imposto = salario_bruto * 0.03
salario_receber = salario_bruto - imposto

print(f"O salário a receber é {round(salario_receber)}")
