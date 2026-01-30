n = int(input())
li = list(map(int,input().split()))
visitas = []
roubados = 0
restam = 0
planetas = 0
for i in li:
    roubados +=1
    li[i] -=1
    

    if li[i] % 2 == 0:
        i = i-1

#inacabado