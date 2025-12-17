matriz = []
counter =0
for i in range(4):
    lista=[]
    for j in range(4):
        x = int(input())
        if x % 2 == 0:
            counter+=1
        lista.append(x)
    matriz.append(lista)

for a in matriz:
    print(a)
print()
print(f"Números pares: {counter}")