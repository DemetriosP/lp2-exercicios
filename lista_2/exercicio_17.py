peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))

imc = peso / (altura ** 2)

if imc <= 17:
    print("Você está muito abaixo do peso")
elif 17 < imc <= 18.49:
    print("Você está abaixo do peso")
elif 18.49 < imc <= 24.99:
    print("Você está com o peso normal")
elif 24.99 < imc <= 29.99:
    print("Você está acima do peso")
elif 24.99 < imc <= 34.99:
    print("Você está com obesidade I")
elif 34.99 < imc <= 39.99:
    print("Você está com obesidade II (severa)")
else:
    print("Você está com obesidade III (mórbida)")
