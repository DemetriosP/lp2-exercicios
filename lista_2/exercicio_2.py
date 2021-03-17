vendas_mensais = float(input("Informe o seu volume mensal de vendas: "))

if vendas_mensais <= 5000:
    comissao = vendas_mensais * 0.02
elif 5000.01 <= vendas_mensais <= 10000:
    comissao = vendas_mensais * 0.05
elif 10000.01 <= vendas_mensais <= 15000:
    comissao = vendas_mensais * 0.07
else:
    comissao = vendas_mensais * 0.09

print(f"A sua comissão referente a este mês é de {round(comissao,2)} reais")
