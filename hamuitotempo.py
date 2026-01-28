n = int(input())
ano = 2015
for i in range(n):
    t = int(input())
    passar = (ano) - t
    if passar<0:
        print(f"{abs(passar-1)} A.C.")
    if passar==0:
        print(f"{1} A.C.")
    if passar>0:
        print(f"{passar} D.C.")
    