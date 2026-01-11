#lista = ["pedra","papel","tesoura","lagarto","Spock"]
n = int(input())
for i in range(1,n+1):
    a,b = input().split()
    if a == "pedra" and (b == "papel"or b =="Spock"):
        print(f"Caso #{i}: Raj trapaceou!")
    elif a == "papel" and (b == "tesoura"or b =="lagarto"):
        print(f"Caso #{i}: Raj trapaceou!")
    elif a == "tesoura" and (b == "pedra"or b =="Spock"):
        print(f"Caso #{i}: Raj trapaceou!")
    elif a == "lagarto" and (b == "pedra"or b =="tesoura"):
        print(f"Caso #{i}: Raj trapaceou!")
    elif a == "Spock" and (b == "lagarto"or b =="papel"):
        print(f"Caso #{i}: Raj trapaceou!")
    elif a == b:
        print(f"Caso #{i}: De novo!")
    else:
        print(f"Caso #{i}: Bazinga!")
    