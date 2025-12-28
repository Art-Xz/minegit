matriz = []
quest = input()
soma = 0.0

for i in range(12):
    linha = []
    for j in range(12):
        x = float(input())
        linha.append(x)
    matriz.append(linha)

for a in range(12):
    for b in range(12):
        if a + b > 11:
            soma+= matriz[a][b]

if quest == "S":
    print(f"{soma:.1f}")
else:
    media = soma/66
    print(f"{media:.1f}")