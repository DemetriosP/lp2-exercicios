racao_comprada = float(input("Informe a quantidade de ração comprada em quilos: "))
racao_comprada = racao_comprada * 1000
racao_fornecida_a = float(input("Informe a quatidade de ração em gramas, fornecida para o gato A: "))
racao_fornecida_b = float(input("Informe a quatidade de ração em gramas, fornecida para o gato B: "))

dias = 0
acabou = 0
racao_faltou = 0

while dias < 5:
    racao_comprada -= (racao_fornecida_a + racao_fornecida_b)

    dias += 1

    if racao_comprada < 0 and acabou == 0:
        dia_racao_acabou = dias
        racao_faltou = racao_comprada
        acabou = 1

print(f"Após 5 dias restará {racao_comprada} gramas") if racao_comprada > 0 else \
    print(f"Após 5 dias a ração acabou, a ração acabou no dia {dias}, "
          f"nesse dia falou {abs(racao_faltou)} gramas de ração")
