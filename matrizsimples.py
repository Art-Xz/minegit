matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        num = int(input())
        linha.append(num)
    matriz.append(linha)

for a in matriz:
    print(a)