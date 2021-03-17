salario = float(input("Informe o valor do salario: "))

if salario <= 600:
    desconto = salario * 0.07
elif 600.01 <= salario <= 800:
    desconto = salario * 0.08
elif 800.01 <= salario <= 1200:
    desconto = salario * 0.09
else:
    desconto = salario * 0.11

print(f"O desconto do INSS com base no seu salario é de {round(desconto,2)} reais")
