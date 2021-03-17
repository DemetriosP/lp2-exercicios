compra = float(input("Informe o valor da compra: "))

if compra <= 100:
    parcelas = 2
    valor_parcela = compra / parcelas
elif 100.01 <= compra <= 200:
    parcelas = 3
    valor_parcela = compra / parcelas
elif 200.01 <= compra <= 400:
    parcelas = 4
    valor_parcela = compra / parcelas
else:
    parcelas = 5
    valor_parcela = compra / parcelas

print(f"A compra pode ser parcelada em {parcelas} parcelas de {round(valor_parcela,2)} reais sem juros")
