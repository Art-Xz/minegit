frase = "LIFE IS NOT A PROBLEM TO BE SOLVED"
counter = 0
frase_ = list(frase)
n = int(input())


for i in frase_:
    if counter == n:
        break
    else:
        print(i,end="")
    counter+=1
print()

