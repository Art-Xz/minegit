n = int(input())
for i in range(n):
    jog1 = input().strip()
    jog2 = input().strip()

    if jog1 == jog2:
        if jog1 == "papel":
            print("Ambos venceram")
        elif jog1 == "pedra":
            print("Sem ganhador")
        elif jog1 == "ataque":
            print("Aniquilacao mutua")
    else:
        if jog1 == "ataque":
            print("Jogador 1 venceu")
        elif jog2 == "ataque":
            print("Jogador 2 venceu")
        
        elif jog1 == "pedra" and jog2 == "papel":
            print("Jogador 1 venceu")
        elif jog2 == "pedra" and jog1 == "papel":
            print("Jogador 2 venceu")