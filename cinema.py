a,b = map(float,input().split())
dif = a-b
porc = abs((dif/a)*100)
print(f"{porc:.2f}%")