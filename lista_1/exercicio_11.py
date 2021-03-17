salario_minimo = float(input("Informe o salario minimo: "))
quilowatts_gastos = float(input("Informe a quantidade de quilowatts gastos: "))
quilowatts = (salario_minimo / 7)

print(f"O custo de cada quilowatts é de {round(quilowatts, 2)} reais")
print(f"O valor a ser pago é de {round(quilowatts_gastos * quilowatts, 2)} reais")
print(f"Valor a ser pago com um desconto de 10% é "
      f"{round((quilowatts_gastos * quilowatts) - ((quilowatts_gastos * quilowatts) * 0.1), 2)} reais")
