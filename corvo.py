counter = 0
soma = 0

while True:
    binario = ""
    entrada = input()
    decimal = 0
    if entrada == "caw caw":
        print(soma)
        counter+=1
        binario = ""
        soma = 0
        if counter == 3:
            break
        continue

    for i in entrada:
        if i == "*":
            binario +="1"
        elif i == "-":
            binario +="0"

    if binario:
        decimal = int(str(binario),2)
        soma +=decimal