matriz = []
soma = 0
range_da_matriz = int(input("Range: "))

for i in range(range_da_matriz):
    lista = []
    for j in range(range_da_matriz):
        x = int(input())
        soma+=x
        lista.append(x)
    matriz.append(lista)

for a in matriz:
    print(a)

print(f"soma dos termos: {soma}")