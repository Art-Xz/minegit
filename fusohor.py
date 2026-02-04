ini,che,fuso = map(int,input().split())
if ini == 0:
    ini = 24

saida = ini+che+fuso

if saida > 23:
    saida-=24

print(saida)