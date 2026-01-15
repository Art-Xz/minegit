n = int(input())
pessoas = list(map(int,input().split()))[:n]
menor_valor = pessoas[0]
posicao_menor = 1
for i in range(1,n):
    if pessoas[i] < menor_valor:
        menor_valor = pessoas[i]
        posicao_menor = i + 1
print(posicao_menor)
    