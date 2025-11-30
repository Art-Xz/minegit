A = []
counter = 0
for i in range(5):
    x = float(input())
    A.append(x)
for c in A:
    if c <= 10:
        print(f"A[{counter}] = {c:.1f}")
    counter +=1