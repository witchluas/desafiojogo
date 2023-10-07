while True:
    jogador1 = input("Digite o nome do jogador 1: ")
    jogador2 = input("Digite o nome do jogador 2: ")

    opcao1 = input(f"{jogador1}, escolha uma opção:\n"
                   "1 - Pedra\n"
                   "2 - Papel\n"
                   "3 - Tesoura\n"
                   "Digite uma opção: ")

    opcao2 = input(f"{jogador2}, escolha uma opção:\n"
                   "1 - Pedra\n"
                   "2 - Papel\n"
                   "3 - Tesoura\n"
                   "Digite uma opção: ")

    while opcao1 not in "123" or opcao2 not in "123":
        print("Opção Inválida!!")

    opcao1 = int(opcao1)
    opcao2 = int(opcao2)

    if opcao1 == opcao2:
        print("EMPATE!!!")
    elif (opcao1 == 1 and opcao2 == 3) or (opcao1 == 2 and opcao2 == 1) or (opcao1 == 3 and opcao2 == 2):
        print(f"{jogador1} VENCEU!!")
    else:
        print(f"{jogador2} VENCEU!!")

    novamente = input("Deseja jogar novamente? (s/n): ")
    if novamente!= 's':
        break