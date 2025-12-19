matriz = []
x = 0
soma_da_diagonal = 0
for i in range(5):
    lista = []
    for j in range(5):
        x +=1
        lista.append(x)
    matriz.append(lista)

for a in matriz:
    print(a)

for b in range(5):
    soma_da_diagonal+=matriz[b][b]
print(f"soma da diagonal = {soma_da_diagonal}")