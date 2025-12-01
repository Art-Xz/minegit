vetor = []
counter = 0
for i in range(20):
    x = int(input())
    vetor.append(x)
vetor = sorted(vetor,reverse=True)
for c in vetor:
    print(f"N[{counter}] = {c}")
    counter+=1


