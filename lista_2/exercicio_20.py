nota_1 = float(input("Informe a primeira nota do aluno: "))
nota_2 = float(input("Informe a segunda nota do aluno: "))
nota_3 = float(input("Informe a terceira nota do aluno: "))
nota_4 = float(input("Informe a quarta nota do aluno: "))

media_1 = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media_1 >= 7:
    print("O aluno foi aprovado")
    print(f"A media do aluno é {round(media_1,2)}")
else:
    nota_5 = float(input("Informe a nota do exame do aluno: "))
    media_2 = (media_1 + nota_5) / 2

    print("Aluno aprovado em exame") if media_2 >= 5 else print("Aluno reprovado")
    print(f"A media do aluno é {round(media_2,2)}")
