numero = 0
numero_maior = 0
numero_menor = 0

while numero > -1:
    numero = int(input("Informe um número: "))

    if numero > numero_maior:
        numero_maior = numero

    if numero_menor > numero >= 0:
        numero_menor = numero

print(f"O maior numero informado foi {numero_maior}")
print(f"O menor numero informado foi {numero_menor}")
