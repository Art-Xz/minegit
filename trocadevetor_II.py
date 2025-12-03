t = int(input())
counter = 0
for i in range(1000):
    if counter > (t -1):
        counter = 0
    print(f"N[{i}] = {counter}")
    counter += 1
    