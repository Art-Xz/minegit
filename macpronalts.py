n = int(input())
valor = 0.0

for i in range(n):
    c,q = map(int,input().split())
    if c == 1001:
        valor+= 1.50*q
    if c == 1002:
        valor+= 2.50*q
    if c == 1003:
        valor+= 3.50*q
    if c == 1004:
        valor+= 4.50*q
    if c == 1005:
        valor+= 5.50*q

print(f"{valor:.2f}")