nome = input("Para começarmos o jogo, informe o seu nome: ")

print(f"Olá {nome}, espero que goste do jogo, boa sorte!\n")

print("Em que ano surgiu a linguagem de programação Python?")
resposta_1 = input("(A) - 1992\n(B) - 1989\n(C) - 1732\n(D) - 2010\n")

print("Quem criou a linguagem de programação Python?")
resposta_2 = input("(A) - Steve Jobs\n"
                   "(B) - Bjarne Stroustrup\n"
                   "(C) - Guido van Rossum\n"
                   "(D) - Ada Lovelace\n")

print("A linguagem de programação Python surgiu em qual país?")
resposta_3 = input("(A) - Estados Unidos\n(B) - Países Baixos\n(C) - França\n(D) - Brasil?\n")

acertos = 0

if resposta_1 == "A":
    acertos += 1
if resposta_2 == "C":
    acertos += 1
if resposta_3 == "B":
    acertos += 1

if acertos == 3:
    print("Parabéns você acertou todas as perguntas")
elif acertos == 2:
    print("Você acertou 2 perguntas")
elif acertos == 1:
    print("Você acertou 1 pergunta")
else:
    print("Infelismente você não acertou nenhuma pergunta")
