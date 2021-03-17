idade = int(input("Informe a idade do nadador: "))

if 5 <= idade <= 7:
    categoria = "infantil A"
elif 8 <= idade <= 10:
    categoria = "infantil B"
elif 11 <= idade <= 13:
    categoria = "juvenil A"
elif 14 <= idade <= 17:
    categoria = "juvenil B"
else:
    categoria = "senior"

print(f"A categoria do nadador é {categoria}")
