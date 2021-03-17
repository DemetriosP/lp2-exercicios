produto = 0

while produto < 1 or produto > 4:
    print("Informe o produto:")
    print("1 - Cesta básica\n2 - Eletrônicos\n3 - Serviços\n4 - Demais produtos\n")
    produto = int(input())

valor_produto = float(input("Informe o valor do produto: "))

imposto = 0

if produto == 1:
    print("Você esta isento de pagar o ICMS")
elif produto == 2:
    imposto = valor_produto * 0.25
elif produto == 3:
    imposto = valor_produto * 0.18
else:
    imposto = valor_produto * 0.12

if imposto > 0:
    print(f"O valor do imposto de ICMS do seu produto é de {round(imposto,2)} reais")
