while True:
    try:
        N = int(input())
        esp = -1
        matriz = []
        for i in range(N):
            linha = []
            for j in range(N):
                linha.append(3)
            matriz.append(linha)
        
        for c in range(N):
            matriz[c][c] = 1
        for d in range(N):
            matriz[d][esp] = 2
            esp -= 1
        
        #--saída
        for a in matriz:
            for b in a:
                print(b,end="")
            print()

    except EOFError:
        break