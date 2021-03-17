distancia_quilometros = float(input("Informe a distancia percorrida pelo objeto em quilometro: "))
tempo_minutos = int(input("Informe o espaço em tempo em minutos: "))

velocidade_projetil = (distancia_quilometros * 100) / (tempo_minutos * 60)

print(f"A velocidade do projetil é de {round(velocidade_projetil)} metros por segundo")
