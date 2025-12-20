matriz = []
x = 0
soma = 0
esp = -1
for i in range(5):
    linha = []
    for j in range(5):
        x+=1
        linha.append(x)
    matriz.append(linha)

for a in matriz:
    print(a)
print()

for b in range(5):
    soma += matriz[b][esp]
    esp = esp - 1
print(soma)
#print(matriz[0][-2])