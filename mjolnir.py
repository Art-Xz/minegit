n = int(input())


for i in range(n):
    nome,força = input().split()
    força_int = int(força)
    if nome ==  "Thor":
        print("Y")
    else:
        print("N")