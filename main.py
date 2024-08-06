nomes=[]
while True:
    print('1 - Inserir novo nome.')
    print('2 - Exibir lista de nomes.')
    print('3 - Exibir em ordem alfabética')
    print('4 - Sair do programa.')

    # opção do usuário
    opcao = input('Opção do usuário:')

    # verifica a opção escolhida
    match opcao:
        case '1':
            novo_nome = input('Insira o novo nome:').capitalize()
            nomes.append(novo_nome)
            print(f'{novo_nome} inserido com sucesso.')
            continue
        case '2':
            print('\nLISTA DE NOMES:\n')
            for nome in nomes:
                print(nome)
            continue
        case '3':
            nomes.sort()
            for nome in nomes:
                print(nome)
                print('Lista ordenada com sucesso.')
            continue
        case '4':
            print('Progarma encerrado.')
            break
        case _:
            print('Opção inválida')