numero_1 = int(input("Informe o primeiro numero: "))
numero_2 = int(input("Informe o segundo numero: "))

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
resto_divisao = numero_1 % numero_2
exponenciacao = numero_1 ** numero_2
radiciacao = numero_1 ** (1/numero_2)

print("\nResultado das seguintes operações realizadas com os numeros informados:\n")
print(f"Soma = {soma}")
print(f"Subtração = {subtracao}")
print(f"Multiplicação = {multiplicacao}")
print(f"Divisão = {round(divisao,2)}")
print(f"Resto da Divisão = {resto_divisao}")
print(f"Exponenciação = {exponenciacao}")
print(f"Radiciação = {round(radiciacao,2)}")
