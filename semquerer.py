while True:
    valor = 0
    y =0
    print()
    matriz = []
    x = int(input())
    if x == 0:
        break

    for i in range(x):
        linha = []
        for j in range(x):
            y +=1
            linha.append(y)
            if len(linha)==x:
                valor+=1
                y= valor
        matriz.append(linha)
    
    for a in matriz:
        print()
        for i in a:
            print(i,end=" ")