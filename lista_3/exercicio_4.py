comecar = 0
janela = [0]*24
corredor = [0]*24
alternativa_1 = 0
alternativa_2 = 0
poltrona = 0

while comecar == 0:

    print("Seja bem vindo")

    while alternativa_1 != 1 and alternativa_1 != 2:
        print("1 - Comprar passagem\n2 - Mostrar mapa de ocupação do ônibus")
        alternativa_1 = int(input())

    if alternativa_1 == 1:

        while alternativa_2 != 1 and alternativa_2 != 2:
            print("1 - Janela\n2 - Corredor")
            alternativa_2 = int(input())

        while poltrona < 1 or poltrona > 24:
            print("Informe o número da poltrona: ")
            poltrona = int(input())

        if janela.count(0) > 0 or corredor.count(0) > 0:

            if janela.count(0) > 1 and alternativa_2 == 1:
                if janela[poltrona-1] == 0:
                    janela[poltrona-1] = 1
                    print("Venda efetivada")
                else:
                    print("Poltrona ocupada")
            elif janela.count(0) == 0 and alternativa_2 == 1:
                print("Todos as poltronas na janela estão ocupadas")

            if corredor.count(0) > 1 and alternativa_2 == 2:
                if corredor[poltrona-1] == 0:
                    corredor[poltrona-1] = 1
                    print("Venda efetivada")
                else:
                    print("Poltrona ocupada")
            elif janela.count(0) == 0 and alternativa_2 == 2:
                print("Todos as poltronas na corredor estão ocupadas")

        else:
            print("ônibus lotado")

        alternativa_2 = 0
        poltrona = 0

    else:
        print(f"Mapa das poltronas da janela\n {janela}")
        print(f"Mapa das poltronas do corredor\n {corredor}")
        input("Precione qualquer teclara para sair...")

    alternativa_1 = 0
