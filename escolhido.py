n = int(input())
maior = ['',-1]
counter = 0
for i in range(n):
    a,b = map(float,input().split())
    if b > maior[1]:
        maior[0] = a
        maior[1] = b
    if maior[1] < 8:
        counter +=1


if counter == n:
    print("Minimum note not reached")
else:
    print(f"{maior[0]:.0f}")
