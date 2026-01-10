while True:
    try:
        n = int(input())
        matriz = []
        limit = n//3
        esp = -1
        espII = 0

        for i in range(n):
            linha=[]
            for j in range(n):
                linha.append(0)
            matriz.append(linha)
        
        for c in range(limit):
            matriz[c][c] = 2
            matriz[n-1-c][n-1-c] = 2
            espII -=1
        for d in range(limit):
            matriz[d][n-1-d] = 3
            matriz[n-1-d][d] = 3
        
        for z in range(n):
            for y in range(n):
                if z >= limit and z < n - limit and y >= limit and y < n-limit:
                    matriz[z][y] = 1
        #numero central--
        if n%2 != 0:
            num = n//2
            matriz[num][num]=4
        

        #--
        for a in matriz:
            for b in a:
                print(b,end="")
            print()
        print()

    except EOFError:
        break