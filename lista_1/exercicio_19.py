valor = float(input("Informe o valor da prestação atrasada: "))
tempo = int(input("Informe a quantos dias a prestação está atrasada: "))
taxa = float(input("Informe a taxa de juros: "))

prestacao = valor + (valor * (taxa/100) * tempo)

print(f"O valor da prestação recalculada é {round(prestacao)}")
