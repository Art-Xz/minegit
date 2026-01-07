while True:
    try:
        N = int(input())
        x = list(map(int,input().split()))
        max_val = max(x)
        if max_val >=20:
            print(3)
        elif max_val >=10:
            print(2)
        if max_val <10:
            print(1)
    except EOFError:
        break
