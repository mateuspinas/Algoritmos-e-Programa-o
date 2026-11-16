
banco_exercicios = ""
programa_rodando = True

while programa_rodando:
    print("\n===== ACADEMIA - EXERCÍCIOS =====\n1 - Cadastrar\n2 - Listar\n3 - Atualizar\n4 - Remover\n0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Até o próximo treino!")
        programa_rodando = False
    elif opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4":
        print("Opção inválida.")
    else:
        total_exercicios = 0
        posicao = -1

        # ---------- READ (opção 2) / mostra os nomes (opções 3 e 4) ----------
        if opcao != "1":
            contador = 0
            nome = grupo = series = repeticoes = carga = ""
            for caractere in banco_exercicios:
                if caractere == "|":
                    contador = contador + 1
                elif caractere == ";":
                    total_exercicios = total_exercicios + 1
                    if opcao == "2":
                        print(str(total_exercicios) + ") " + nome + " | Grupo: " + grupo + " | " + series + "x" + repeticoes + " | Carga: " + carga + " kg")
                    else:
                        print(str(total_exercicios) + ") " + nome)
                    contador = 0
                    nome = grupo = series = repeticoes = carga = ""
                elif contador == 0:
                    nome = nome + caractere
                elif contador == 1:
                    grupo = grupo + caractere
                elif contador == 2:
                    series = series + caractere
                elif contador == 3:
                    repeticoes = repeticoes + caractere
                else:
                    carga = carga + caractere
            if total_exercicios == 0:
                print("Nenhum exercício cadastrado.")

            # escolha do exercício (opções 3 e 4)
            if (opcao == "3" or opcao == "4") and total_exercicios > 0:
                escolha = input("Número do exercício: ")
                valido = escolha != ""
                for caractere in escolha:
                    if caractere not in "0123456789":
                        valido = False
                if valido and (int(escolha) < 1 or int(escolha) > total_exercicios):
                    valido = False
                if valido:
                    posicao = int(escolha) - 1
                else:
                    print("Número inválido.")

        # ---------- CREATE (1) / UPDATE (3) / DELETE (4) ----------
        if opcao == "1" or posicao >= 0:
            registros_anteriores = ""
            registros_posteriores = ""
            nome_exercicio = grupo_exercicio = series_exercicio = repeticoes_exercicio = carga_exercicio = ""

            if posicao >= 0:  # separa os registros antes e depois do escolhido e pega os campos dele
                indice = 0
                contador = 0
                nome = grupo = series = repeticoes = carga = ""
                for caractere in banco_exercicios:
                    if caractere == "|":
                        contador = contador + 1
                    elif caractere == ";":
                        registro = nome + "|" + grupo + "|" + series + "|" + repeticoes + "|" + carga + ";"
                        if indice < posicao:
                            registros_anteriores = registros_anteriores + registro
                        elif indice == posicao:
                            nome_exercicio = nome
                            grupo_exercicio = grupo
                            series_exercicio = series
                            repeticoes_exercicio = repeticoes
                            carga_exercicio = carga
                        else:
                            registros_posteriores = registros_posteriores + registro
                        indice = indice + 1
                        contador = 0
                        nome = grupo = series = repeticoes = carga = ""
                    elif contador == 0:
                        nome = nome + caractere
                    elif contador == 1:
                        grupo = grupo + caractere
                    elif contador == 2:
                        series = series + caractere
                    elif contador == 3:
                        repeticoes = repeticoes + caractere
                    else:
                        carga = carga + caractere

            if opcao == "4":
                if input("Remover '" + nome_exercicio + "'? (s/n): ") == "s":
                    banco_exercicios = registros_anteriores + registros_posteriores
                    print("Exercício removido!")
                else:
                    print("Remoção cancelada.")
            else:
                if opcao == "3":
                    print("(Deixe em branco para manter o valor atual)")
                for campo in range(5):  # 0 nome, 1 grupo, 2 séries (int), 3 repetições (int), 4 carga (float)
                    if campo == 0:
                        rotulo = "Nome do exercício"
                        atual = nome_exercicio
                    elif campo == 1:
                        rotulo = "Grupo muscular"
                        atual = grupo_exercicio
                    elif campo == 2:
                        rotulo = "Séries"
                        atual = series_exercicio
                    elif campo == 3:
                        rotulo = "Repetições"
                        atual = repeticoes_exercicio
                    else:
                        rotulo = "Carga (kg)"
                        atual = carga_exercicio
                    if opcao == "3":
                        rotulo = rotulo + " (atual: " + atual + ")"
                    lendo = True
                    while lendo:
                        texto = input(rotulo + ": ")
                        texto_limpo = ""
                        for caractere in texto:
                            if caractere == "," and campo > 1:
                                texto_limpo = texto_limpo + "."
                            elif caractere == "|" or caractere == ";":
                                texto_limpo = texto_limpo + "-"
                            else:
                                texto_limpo = texto_limpo + caractere
                        valido = True
                        if texto_limpo == "":
                            if opcao == "3":
                                texto_limpo = atual
                            elif campo != 1:
                                valido = False
                        elif campo > 1:
                            pontos = 0
                            digitos = 0
                            for caractere in texto_limpo:
                                if caractere == ".":
                                    pontos = pontos + 1
                                elif caractere in "0123456789":
                                    digitos = digitos + 1
                                else:
                                    valido = False
                            if digitos == 0 or pontos > 1 or (campo < 4 and pontos > 0):
                                valido = False
                        if valido:
                            if campo == 0:
                                nome_exercicio = texto_limpo
                            elif campo == 1:
                                grupo_exercicio = texto_limpo
                            elif campo == 2:
                                series_exercicio = str(int(texto_limpo))
                            elif campo == 3:
                                repeticoes_exercicio = str(int(texto_limpo))
                            else:
                                carga_exercicio = str(float(texto_limpo))
                            lendo = False
                        elif campo == 0:
                            print("O nome não pode ficar vazio.")
                        elif campo < 4:
                            print("Valor inválido: digite um número inteiro.")
                        else:
                            print("Valor inválido: digite um número (ex.: 12.5).")
                registro = nome_exercicio + "|" + grupo_exercicio + "|" + series_exercicio + "|" + repeticoes_exercicio + "|" + carga_exercicio + ";"
                if opcao == "1":
                    banco_exercicios = banco_exercicios + registro
                    print("Exercício cadastrado com sucesso!")
                else:
                    banco_exercicios = registros_anteriores + registro + registros_posteriores
                    print("Exercício atualizado!")
