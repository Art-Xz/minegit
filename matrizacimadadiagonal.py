matriz = []
num = -1
soma = 0.0
lista = []
for i in range(12):
    linha = []
    for j in range(12):
        num +=1
        #num = float(input())
        linha.append(num)
    matriz.append(linha)


for a in range(12):
    lista.append(matriz[a][a])
print(lista)
for b in range(12):
    for c in range(12):
        if c>b:
            soma+=matriz[b][c]
print(soma)