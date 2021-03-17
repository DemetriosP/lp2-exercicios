nota_1, nota_2, nota_3 = float(input("Informe a primeira nota: ")), \
                         float(input("Informe a segunda nota: ")), \
                         float(input("Informe a terceira nota: "))

peso_1, peso_2, peso_3 = float(input("Informe o peso da primeira nota: ")), \
                         float(input("Informe o peso da segunda nota: ")), \
                         float(input("Informe o peso da terceira nota: "))

media = (nota_1 * peso_1 + nota_2 * peso_2 + nota_3 * peso_3) / (peso_1 + peso_2 + peso_3)

print(f"Nota 1: {nota_1}\nNota 2: {nota_2}\nNota 3: {nota_3}")
print(f"Peso 1: {peso_1}\nPeso 2: {peso_2}\nPeso 3: {peso_3}")
print(f"Média ponderada: {round(media, 2)}")

