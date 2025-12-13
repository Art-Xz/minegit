N = int(input())
counter = 1
test = int(input())
for i in range(N-1):
    C = int(input())
    if C != test:
        counter +=1
    test = C

print(counter)

