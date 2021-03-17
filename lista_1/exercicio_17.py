valor_pagar = float(input("Informe o valor daa conta a ser paga: "))

nota_cinquenta = 0
nota_dez = 0
nota_um = 0

while valor_pagar >= 50:
    valor_pagar -= 50
    nota_cinquenta += 1

while valor_pagar >= 10:
    valor_pagar -= 10
    nota_dez += 1

while valor_pagar >= 1:
    valor_pagar -= 1
    nota_um += 1

print(f"Será necessario {nota_cinquenta} notas de 50, {nota_dez} notas de 10 e {nota_um} notas de 1 para pagar a conta")
