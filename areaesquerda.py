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

for colunas in range(12):
    for linhas in range(12):
        if colunas<linhas and colunas+linhas < 11:
            soma += matriz[linhas][colunas]
            counter+=1

if quest == "S":
    print(f"{soma:.1f}")
else:
    media  = soma/counter
    print(f"{media:.1f}")