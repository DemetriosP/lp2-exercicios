valor_hora_aula = int(input("Informe o valor da hora aula: "))
numero_aula_mes = int(input("Informe o numero de aulas dadas no mês: "))
percentual_desconto_inss = float(input("Informe o percentaul de desconto do INSS: "))

hora_aula_liquida = valor_hora_aula - (valor_hora_aula * (percentual_desconto_inss / 100))
salario = numero_aula_mes * hora_aula_liquida

print(f"O valor da hora aula liquida é de {hora_aula_liquida} reais")
print(f"O valor a receber nesse mês é de {salario} reais")