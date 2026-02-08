n,m = map(int,input().split())
init = n

for i in range(5):
    acao= input()
    if acao == "fechou":
        init-=1
        init+=2
    if acao == "clicou":
        init-=1

print(init)