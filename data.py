while True:
    try:
        ano = [31,29,31,30,31,30,31,31,30,31,30,31]
        total = 360
        dias = 0
        counter = 0
        mes,dia = map(int,input().split())

        if mes == 12 and dia == 24:
            print("E vespera de natal!")
        elif mes == 12 and dia == 25:
            print("E natal!")
        elif mes == 12 and dia > 25:
            print("Ja passou!")
        else:
            resto = 0
            passaram = 0
            for i in range(mes-1):
                passaram+= ano[i]
            passaram+=dia
            resto = total - passaram
            print(f"Faltam {resto} dias para o natal!")
    except EOFError:
        break
