fat_empresa = 0
cons_paga_500_1000 = 0

salario = float(input("Informe o valor do salario minimo: "))

while True:

    quant_quilowatts = float(input("Informe a quantidade de quilowatts gasta: "))
    if quant_quilowatts == 0:
        break

    tipo_consumidor = input("Informe o tipo de consumidor:\n1-Residencial\n2-Comercial\n3-Industrial\n")

    valor_pago_consumidor = (salario / 1600) * quant_quilowatts

    if tipo_consumidor == "1":
        acrescimo = valor_pago_consumidor * 0.05
    elif tipo_consumidor == "2":
        acrescimo = valor_pago_consumidor * 0.10
    else:
        acrescimo = valor_pago_consumidor * 0.15

    valor_pago_consumidor += acrescimo

    print(f"O valor a ser pago pelo consumidor: {round(valor_pago_consumidor,2)}")

    fat_empresa += valor_pago_consumidor

    if 500 <= valor_pago_consumidor <= 100:
        cons_paga_500_1000 += 1

print(f"O valor de cada quilowatt: {round(salario/1600,2)}")
print(f"Faturamento da empresa: {round(fat_empresa,2)}")
print(f"Quantidade de consumidores que pagam entre R$ 500.00 e R$ 1000.00: {cons_paga_500_1000}")
