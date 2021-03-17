soma = 0
dividir = 0

for i in range(50, 71):
    if i % 2 == 0:
        soma += i
        dividir += 1

media = soma / dividir

print(f"A soma dos numeros pares na faixa de 50 e 70 é {soma}")
print(f"A média aritimética dos numeros pares na faixa de 50 a 70 é {media}")
