num = int(input())
def int_to_roman(num):
    val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    simb = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    saida = ''
    i = 0
    while num > 0:
        for j in range(num//val[i]):
            saida+=simb[i]
            num-= val[i]
        i+=1
    return saida

print(int_to_roman(num))