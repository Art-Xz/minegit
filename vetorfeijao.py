
vetor = []
a, b, c, d = map(int, input().split())
vetor.extend([a,b,c,d])
counter = 0
for i in vetor:
    if i == 0:
        counter+=1
    if i == 1:
        counter +=1
        print(counter)
        break
