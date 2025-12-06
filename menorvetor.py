n = int(input())


x = list(map(int,input().split()))


valor_menor = x[0]
posicao= 0
ind = 0
for valor in x:
    if valor < valor_menor:
        valor_menor = valor
        posicao = ind
    ind +=1    
print("menor valor: ",valor_menor)
print("Posição: ",posicao)
    
    