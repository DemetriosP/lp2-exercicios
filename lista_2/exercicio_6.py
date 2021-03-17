compra = float(input("Informe o valor da compra: "))

if compra <= 50:
    desconto = compra * 0.05
elif 50.01 <= compra <= 100:
    desconto = compra * 0.08
elif 100.01 <= compra <= 150:
    desconto = compra * 0.12
else:
    desconto = compra * 0.15

print(f"O valor do desconto é de {round(desconto,2)} reais")
