numero = 0

while numero <= 0:
    numero = int(input("Informe um numero positivo maior que zero: "))

print(f"Número ao quadrado: {pow(numero, 2)}")
print(f"Número ao cubo: {pow(numero, 3)}")
print(f"Raiz quadrada do número: {pow(numero, (1/2))}")
print(f"Raiz cubica do número: {round(pow(numero, (1/3)), 2)}")
print(f"Soma do quadrado mais o cubo do número: {(pow(numero, 2)) + (pow(numero, 3))}")
