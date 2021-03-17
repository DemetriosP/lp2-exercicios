num_1 = float(input("Informe o primeiro numero: "))
num_2 = float(input("Informe o segundo numero: "))
print("Informe uma das operações")
operacao = input("1 - Soma\n2 - Subatração\n3 - Multiplicação\n4 - Divisão\n")

if operacao == "1":
    resultado = num_1 + num_2
elif operacao == "2":
    resultado = num_1 - num_2
elif operacao == "3":
    resultado = num_1 * num_2
else:
    resultado = num_1 / num_2

print(f"O resultado da sua conta é {round(resultado,2)}")
