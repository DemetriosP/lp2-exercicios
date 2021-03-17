nota_1, nota_2, nota_3 = float(input("Informe a primeira nota: ")), \
                         float(input("Informe a segunda nota: ")), \
                         float(input("Informe a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

print(f"Primeira nota: {nota_1} ")
print(f"Segunda nota: {nota_2} ")
print(f"Terceira nota: {nota_3} ")
print(f"Media das notas: {round(media, 2)}")

