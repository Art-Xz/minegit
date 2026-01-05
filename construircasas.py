while True:
    try:
        a,b,c = map(int,input().split())
        area = a*b

        ladoquadrado = (area*100)/c
        ladoquadrado = ladoquadrado**0.5
        print(int(ladoquadrado))
    except ValueError:
        break