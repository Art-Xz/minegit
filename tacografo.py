valor_total = 0

n = int(input())
for i in range(n):
    T,V = map(int,input().split())
    valor_total += T*V
print(valor_total)
