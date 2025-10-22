#exercício 1042 nível 2
#imprime os valores em ordem crescente e imprimir na ordem original
a,b,c = map(int,input().split())

if a < b and a < c:
    print(a)
    if b < c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)
if b < a and b < c:
    print(b)
    if a < c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
if c < b and c < a:
    print(c)
    if b < a:
        print(b)
        print(a)
    else:
        print(a)
        print(b)

print()
print(a)
print(b)
print(c)