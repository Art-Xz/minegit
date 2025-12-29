matriz = []
soma = 0.0
quest = input()
counter = 0
for i in range(12):
    linha = []
    for j in range(12):
        x = float(input())
        linha.append(x)
    matriz.append(linha)

for a in range(12):
    for b in range(12):
        if b>a and a+b < 11:
            soma+= matriz[a][b]
            counter+=1
if quest == "S":
    print(f"{soma:.1f}")
else:
    media = soma/counter
    print(f"{media:.1f}")

        