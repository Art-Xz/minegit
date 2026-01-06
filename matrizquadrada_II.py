while True:
    y =0
    matriz = []
    x = int(input())
    if x == 0:
        break
    for i in range(x):
        for j in range(x):
            valor = abs(i-j)+1
            if j == 0:
                print(f"{valor:>3}",end="")
            else:
                print(f" {valor:>3}",end="")
        print()
    print()