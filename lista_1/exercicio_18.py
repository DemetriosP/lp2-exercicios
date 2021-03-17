import math

velocidade = float(input("Informe a velocidade do projétil: "))
angulo = float(input("Informe o ângulo entre o cano do canhão e o solo: "))
gravidade = float(input("Informe a gravidade: "))

alcance_projetil = ((velocidade * velocidade) / gravidade) * (math.sin(angulo) * (2 * math.radians(angulo)))

print(f"O alcance do projetil é de {round(alcance_projetil)}")
