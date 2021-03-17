salario = float(input("Informe o valor do salario: "))

desconto = 0

if salario <= 1250:
    print("Você está isento de pagar o IR")
elif 1250.01 <= salario <= 1900:
    desconto = salario * 0.11
elif 1900.01 <= salario <= 2700:
    desconto = salario * 0.25
else:
    desconto = salario * 0.275

if desconto > 0:
    print(f"O desconto do IR com base no seu salario é de {round(desconto,2)} reais")
