# CRUD de exercícios de academia
# somente com while, for, if, elif, else e variáveis (listas paralelas como "banco de dados")

nomes = []
grupos = []
series = []
repeticoes = []
cargas = []

rodando = True

while rodando:
    print("\n===== ACADEMIA - EXERCÍCIOS =====")
    print("1 - Cadastrar exercício")
    print("2 - Listar exercícios")
    print("3 - Atualizar exercício")
    print("4 - Remover exercício")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    # ---------- CREATE ----------
    if opcao == "1":
        nome = input("Nome do exercício: ")
        grupo = input("Grupo muscular: ")
        serie = input("Número de séries: ")
        rep = input("Repetições por série: ")
        carga = input("Carga (kg): ")

        if nome == "":
            print("O nome não pode ficar vazio.")
        else:
            nomes = nomes + [nome]
            grupos = grupos + [grupo]
            series = series + [serie]
            repeticoes = repeticoes + [rep]
            cargas = cargas + [carga]
            print("Exercício cadastrado com sucesso!")

    # ---------- READ ----------
    elif opcao == "2":
        if len(nomes) == 0:
            print("Nenhum exercício cadastrado.")
        else:
            print("\n--- Lista de exercícios ---")
            for i in range(len(nomes)):
                print(str(i + 1) + ") " + nomes[i]
                      + " | Grupo: " + grupos[i]
                      + " | " + series[i] + "x" + repeticoes[i]
                      + " | Carga: " + cargas[i] + " kg")

    # ---------- UPDATE ----------
    elif opcao == "3":
        if len(nomes) == 0:
            print("Nenhum exercício para atualizar.")
        else:
            for i in range(len(nomes)):
                print(str(i + 1) + ") " + nomes[i])
            escolha = input("Número do exercício a atualizar: ")

            valido = True
            if escolha == "":
                valido = False
            for letra in escolha:
                if letra not in "0123456789":
                    valido = False

            if valido:
                pos = int(escolha) - 1
                if pos >= 0 and pos < len(nomes):
                    print("(Deixe em branco para manter o valor atual)")
                    novo_nome = input("Novo nome [" + nomes[pos] + "]: ")
                    novo_grupo = input("Novo grupo [" + grupos[pos] + "]: ")
                    nova_serie = input("Novas séries [" + series[pos] + "]: ")
                    nova_rep = input("Novas repetições [" + repeticoes[pos] + "]: ")
                    nova_carga = input("Nova carga [" + cargas[pos] + "]: ")

                    if novo_nome != "":
                        nomes[pos] = novo_nome
                    if novo_grupo != "":
                        grupos[pos] = novo_grupo
                    if nova_serie != "":
                        series[pos] = nova_serie
                    if nova_rep != "":
                        repeticoes[pos] = nova_rep
                    if nova_carga != "":
                        cargas[pos] = nova_carga
                    print("Exercício atualizado!")
                else:
                    print("Número fora da lista.")
            else:
                print("Digite um número válido.")

    # ---------- DELETE ----------
    elif opcao == "4":
        if len(nomes) == 0:
            print("Nenhum exercício para remover.")
        else:
            for i in range(len(nomes)):
                print(str(i + 1) + ") " + nomes[i])
            escolha = input("Número do exercício a remover: ")

            valido = True
            if escolha == "":
                valido = False
            for letra in escolha:
                if letra not in "0123456789":
                    valido = False

            if valido:
                pos = int(escolha) - 1
                if pos >= 0 and pos < len(nomes):
                    confirma = input("Remover '" + nomes[pos] + "'? (s/n): ")
                    if confirma == "s":
                        novos_nomes = []
                        novos_grupos = []
                        novas_series = []
                        novas_repeticoes = []
                        novas_cargas = []
                        for i in range(len(nomes)):
                            if i != pos:
                                novos_nomes = novos_nomes + [nomes[i]]
                                novos_grupos = novos_grupos + [grupos[i]]
                                novas_series = novas_series + [series[i]]
                                novas_repeticoes = novas_repeticoes + [repeticoes[i]]
                                novas_cargas = novas_cargas + [cargas[i]]
                        nomes = novos_nomes
                        grupos = novos_grupos
                        series = novas_series
                        repeticoes = novas_repeticoes
                        cargas = novas_cargas
                        print("Exercício removido!")
                    else:
                        print("Remoção cancelada.")
                else:
                    print("Número fora da lista.")
            else:
                print("Digite um número válido.")

    # ---------- SAIR ----------
    elif opcao == "0":
        print("Até o próximo treino!")
        rodando = False

    else:
        print("Opção inválida.")
