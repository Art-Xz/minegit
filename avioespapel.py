#https://judge.beecrowd.com/pt/problems/view/2339

C,F,Qtd = map(int,input().split())

comp = F/Qtd
if comp < C:
    print("N")
if comp >= C:
    print("S")