N = int(input())

for i in range(N):
    r1,r2 = map(int,input().split())

    d1 = r1*2
    d2 = r2*2
    DiametroT = d1 + d2
    RaioT = DiametroT/2
    print(f"{RaioT:.0f}")