agenda = {"Pedro": "3214-0098", "Ana": "3245-6578"}


while True:
    print(
        """
            agendinha v 0.1
            escolha uma opcao
            0 - sair
            1 - Criar novo contato
            2 - Listar contatos
            3 - apagar contato
            4 - atualizar contat
        """
    )
    op = int(input(":-) "))

    if op == 0:
        print("tchau")
        break
    elif op == 1:
        nome = input("Informe o nome do contato:")
        tel = input("Telefone:")
        agenda[nome] = tel

    elif op == 2:
        for nome, tel in agenda.items():
            print(f"{nome} - {tel}")

    elif op == 3:
        nome = input("Informe o nome do contato:")

        if nome in agenda.keys():
            for chave in agenda.keys():
                if chave == nome:
                    del agenda[chave]
                    print("Contato apagado com sucesso")
                    break
        else:
            print("Nome não encontrado , tente novamente")

    elif op == 4:
        nome = input("Informe o nome do contato:")
        for chave in agenda.keys():
            if chave == nome:
                print("Vc quer alterar o nome(1) ou o telefone(2), TODOS(3)")
                op2 = int(input(">"))
                if op2 == 1:
                    novo_nome = input("Novo nome:")
                    agenda[i][0] = novo_nome
                elif op2 == 2:
                    novo_tel = input("Novo telefone:")
                    agenda[i][1] = novo_tel
                elif op2 == 3:
                    novo_nome = input("Novo nome:")
                    agenda[i][0] = novo_nome
                    novo_tel = input("Novo telefone:")
                    agenda[i][1] = novo_tel
                else:
                    print("Comando nao cadastrado")
    else:
        print("Comando não cadastrado")
