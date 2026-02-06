num = int(input())
nums = list(map(int,input().split()))
div2= 0
div3= 0
div4= 0
div5= 0
for i in nums:
    if i % 2 == 0:
        div2+=1
    if i % 3 == 0:
        div3+=1
    if i % 4 == 0:
        div4+=1
    if i % 5 == 0:
        div5+=1

print(f'''{div2} Multiplo(s) de 2
{div3} Multiplo(s) de 3
{div4} Multiplo(s) de 4
{div5} Multiplo(s) de 5''')