from random import *

numeros_sorteados = []
frequencia = []
dado_lado = 1

for i in range(0, 20):
    numeros_sorteados.append(randint(1, 6))

while dado_lado < 7:
    if numeros_sorteados.count(dado_lado) > 0:
        print(f"O numero {dado_lado} aparece {numeros_sorteados.count(dado_lado)} vezes")
    dado_lado += 1
