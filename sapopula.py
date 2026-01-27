p,n = map(int,input().split())
inte = False
canos = list(map(int,input().split()))

for i in range(1,n):
    if abs(canos[i] - canos[i-1])>p:
        inte = True
        break

if inte:
    print("GAME OVER")
else:
    print("YOU WIN")