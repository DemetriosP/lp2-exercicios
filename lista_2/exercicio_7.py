empreestimo = float(input("Informe o valor do emprestimo: "))
parcelas = int(input("Informe o numero de parcelas: "))

if parcelas <= 3:
    juros = empreestimo * 0.06
elif 4 <= empreestimo <= 6:
    juros = empreestimo * 0.09
elif 7 <= empreestimo <= 12:
    juros = empreestimo * 0.22
else:
    juros = empreestimo * 0.34

print(f"O valor dos juros é de {round(juros,2)} reais")
