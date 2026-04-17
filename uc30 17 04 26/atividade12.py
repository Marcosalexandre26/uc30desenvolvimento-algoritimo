while True:
    print("\n1-Soma  2-Subtração  3-Multiplicação  4-Divisão  5-Sair")

    try:
        op = int(input("Opção: "))

        if op == 5:
            print("Saindo...")
            break

        n1 = float(input("Número 1: "))
        n2 = float(input("Número 2: "))

        if op == 1:
            print(n1 + n2)
        elif op == 2:
            print(n1 - n2)
        elif op == 3:
            print(n1 * n2)
        elif op == 4:
            if n2 != 0:
                print(n1 / n2)
            else:
                print("Erro: divisão por zero")
        else:
            print("Opção inválida")

    except:
        print("Digite apenas números")