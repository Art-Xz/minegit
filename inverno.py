a,b,c = map(int,input().split())

if b<a:
    print(":)" if c<=b or abs(b-c)<abs(a-b) else ":(")
elif b > a:
    print(":)" if c >= b or abs(b-c)<abs(a-b) else ":(")
else:
    print(":)"if c > b else ":(")
