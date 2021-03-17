sexo_masculino = 0
sexo_feminino = 0
idade_media_mas = 0
homem_maior_45 = 0
mulher_menor_21 = 0
menor_idade_mulher = 0
homem_experiencia = 0

while True:

    idade = int(input("Informe a idade do candidato: "))
    if idade == 0:
        break

    sexo = input("Informe o sexo do candidato:\nM para masculino\nF para feminino\n")
    experiencia = input("O candidato tem experiencia no serviço:\nS para sim\nN para não\n")

    if sexo == "M":
        sexo_masculino += 1
        if experiencia == "S":
            idade_media_mas += idade
            homem_experiencia += 1
            if idade > 45:
                homem_maior_45 += 1
    else:
        sexo_feminino += 1
        if menor_idade_mulher < idade or menor_idade_mulher == 0:
            menor_idade_mulher = idade
            if idade < 21 and experiencia == "S":
                mulher_menor_21 += 1

print(f"Quantidade de candidatos do sexo feminino: {sexo_feminino}")
print(f"Quantidade de candidatos do sexo masculino: {sexo_masculino}")

if idade > 0:
    print(f"Idade média dos homens que tem experiência: {round(idade_media_mas/homem_experiencia,2)}")
    print(f"Porcentagem dos homens com mais de 45 anos entre o total dos homens: "
          f"{(100 * homem_maior_45) / sexo_masculino}")

print(f"Número de mulheres com idade inferior a 21 anos e com experiência: {mulher_menor_21}")
print(f"Menor idade entre as muçheres que já tem experiência: {menor_idade_mulher}")
