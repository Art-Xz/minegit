while True:
    try:
        volume = float(input())
        diametro = float(input())
        PI = 3.14

        r = diametro/2
        h = volume/(PI*(r**2))
        a = PI*(r**2)
        print(f"ALTURA = {h:.2f}")
        print(f"AREA = {a:.2f}")

    except EOFError:
        break