while True:
    matriz = []
    x = int(input())
    if x == 0:
        break
    maior_valor = 2**(2*x-2)
    num_d = len(str((maior_valor)))
    for i in range(x):
        linha = []
        for j in range(x):
            valor = 2**(i+j)
            linha.append(valor)
        matriz.append(linha)
    
    for a in range(x):
        for b in range(x):
            if b == 0:
                print(f"{matriz[a][b]:>{num_d}}",end="")
            else:
                print(f" {matriz[a][b]:>{num_d}}",end="")
        print()
    print()