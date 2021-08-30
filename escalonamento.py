""" Mostra a matriz """
def showMatriz(matriz):
    for linha in matriz:
        print(linha)
        

""" Cria matriz """
def createMatriz():
    
    for i in range(m):
        linha = []
        for j in range(n):
            elemento = input(f"Digite o valor para linhas {i} coluna {j}: ")
            linha.append(float(elemento))
        matriz.append(linha)

""" Faz uma operacao em uma linhas especifica """
def operationInLine():
    print()
    line = int(input("Digite qual o numero da linha que deseja fazer a operacao e qual operacao"))
    print("Escolha qual operacao deseja fazer")
    print("1.Multiplicacao")
    print("2.Divisao")
    operacao = int(input())

    esc = float(input(f"Digite por qual numero deseja " + f"multiplicar a linha {line}" if operacao==1 else f"dividir a linha {line}"))

    if operacao == 1:
        for i in range(n):
            matriz[n][line] = matriz[n][line] * esc
    elif operacao == 2:
        for i in range(n):
            matriz[n][line] = matriz[n][line] / esc
    



m = int(input("Digite o numero de linhas: "))
n = int(input("Digite o numero de colunas: "))

matriz = []
createMatriz()



while True:
    print("-"*30)
    print("Digite a operacao que deseja fazer na matriz: ")
    print("-"*30)
    print("1.Fazer uma operacao em uma linha")
    print("2.Fazer uma operacao entre duas linhas")
    print("3.Sair")
    print("-"*30)

    showMatriz(matriz)
    opcao = int(input("Escolho a opcao: "))

    if opcao == 1:
      
        print()
        line = int(input("Digite qual o numero da linha que deseja fazer a operacao e qual operacao: "))
        line = line-1
        print("Escolha qual operacao deseja fazer: ")
        print("1.Multiplicacao")
        print("2.Divisao")
        operacao = int(input())

        if operacao == 1:
            esc = float(input(f"Digite por qual numero deseja multiplica a linha {line+1}: "))
        else:
            esc = float(input(f"Digite por qual numero deseja dividir a linha {line+1}: "))

        if operacao == 1:
            for i in range(n):
                matriz[line][i] = matriz[line][i] * esc
        elif operacao == 2:
            for i in range(n):
                matriz[line][i] = matriz[line][i] / esc
        
        showMatriz(matriz)

    elif opcao == 2:
        print()

        print(f"L? = L? ? L?")

        lr = int(input("Selecione qual linha ira receber a operacao: "))
        lr = lr-1
        print(f"L{lr+1} = L? ? L?")

        l1 = int(input("Selecione a primeira linha da operacao: "))
        l1 = l1-1
        print(f"L{lr+1} = L{l1+1} ? L?")

        l2 = int(input("Selecione a segunda linha da operacao: "))
        l2 = l2-1
        print(f"L{lr+1} = L{l1+1} ? L{l2+1}")

        print("Selecione qual operacao sera feita entre elas")
        print("1.Adicao")
        print("2.Subtracao")

        operacaoEntreMatrizes = int(input())

        print(f"L{lr+1} = L{l1+1} + L{l2+1}") if operacaoEntreMatrizes == 1 else (f"L{lr+1} = L{l1+1} - L{l2+1}")

        if operacaoEntreMatrizes == 1:
            for i in range(n):
                matriz[i][lr] = matriz[i][l1] + matriz[i][l2]
        else:
            for i in range(n):
                matriz[i][lr] = matriz[i][l1] - matriz[i][l2]

        showMatriz(matriz)
    
    if opcao == 3:
        break





