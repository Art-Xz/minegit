matriz = []
soma = 0.0
lista = []
x = input()
for i in range(12):
    linha = []
    for j in range(12):
        
        num = float(input())
        linha.append(num)
    matriz.append(linha)

for b in range(12):
    for c in range(12):
        if c>b:
            soma+=matriz[b][c]

if x == "S":
    print(f"{soma:.1f}")
else:
    media = soma/66
    print(f"{media:.1f}")