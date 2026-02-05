p,j1,j2,r,a = map(int,input().split())

if p == 0:
    jog_impar = "Jogador 1 ganha!"
    jog_par = "Jogador 2 ganha!"
if p == 1:
    jog_impar = "Jogador 2 ganha!"
    jog_par = "Jogador 1 ganha!"

if r == 0 and a == 0:
    soma = j1+j2
    if soma % 2 == 0:
        print(jog_par)
    else:
        print(jog_impar)
else:
    if r == 1 and a == 0:
        print("Jogador 1 ganha!")
    if r == 0 and a == 1:
        print("Jogador 1 ganha!")
    if r == 1 and a == 1:
        print("Jogador 2 ganha!")

