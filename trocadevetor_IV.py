par = []
impar = []
check = 0
for i in range(15):
    if len(par) == 5:
        counterP = 0
        for p in par:
            print(f"par[{counterP}] = {p}")
            counterP +=1
            check +=1
        par = []
    if len(impar) ==  5:
        counterI = 0
        for m in impar:
            print(f"impar[{counterI}] = {m}")
            counterI +=1
            check +=1
        impar = []
    x = int(input())
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
    if check ==2:
        break
#imprimir tudo---

counterI = 0
for c in impar:
    print(f"impar[{counterI}] = {c}")
    counterI +=1

counterP = 0
for d in par:
    print(f"par[{counterP}] = {d}")
    counterP +=1
