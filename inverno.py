a,b,c = map(int,input().split())

if(b<a and c>=b):
    print(":)")
elif(b>a and c<=b):
    print(":(")
elif(b>a and c >b and c-b<b-a):
    print(":(")
elif(b>a and c >b and c-b>=b-a):
    print(":)")
elif(b<a and c<b and b-c < a-b):
    print(":)")
elif(b<a and c<b and b-c >= a-b):
    print(":(")
elif(a==b):
    if(c>b):
        print(":)")
    else:
        print(":(")

