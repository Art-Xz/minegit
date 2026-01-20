n = int(input())

for i in range(n):
    nome1,esc1,nome2,esc2 = map(str,input().split())
    if esc1 == "PAR":
        par = nome1
    else:
        impar = nome1
    if esc2 == "PAR":
        par = nome2
    else:
        impar = nome2
    
    num1,num2 = map(int,input().split())
    soma = num1 + num2
    if soma % 2 == 0:
        print(par)
    else:
        print(impar)
