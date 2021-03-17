nota_fiscal = float(input("Informe o valor da nota fiscal de serviço: "))

if nota_fiscal <= 5000:
    imposto = nota_fiscal * 0.04
elif 5000.01 <= nota_fiscal <= 10000:
    imposto = nota_fiscal * 0.06
elif 10000.01 <= nota_fiscal <= 20000:
    imposto = nota_fiscal * 0.13
else:
    imposto = nota_fiscal * 0.16

print(f"O valor do ISS com base no valor da nota fiscal é de {round(imposto,2)} reais")
