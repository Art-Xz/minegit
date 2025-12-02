x = int(input())
for i in range(x):
    fibo = [0,1]
    nemes = int(input())
    if nemes == 0:
        print(f"Fib(0) = 0")
    elif nemes == 1:
        print("Fib(1) = 1")
    else:
        for c in range(1,nemes):
            termo = fibo[c] + fibo[c-1]
            fibo.append(termo)
        print(f"Fib({nemes}) = {fibo[-1]}")
    