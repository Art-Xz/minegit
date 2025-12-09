indice = int(input())
operacao = input()
matriz = []
soma = 0.0
for i in range(12):
    linha = []
    for c in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

for j in range(12):
    soma+=matriz[j][indice]

if operacao == "S":
    print(f"{soma:.1f}")
if operacao == "M":
    media = soma/12
    print(f"{media:.1f}")