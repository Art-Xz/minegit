def para_minutos(horario):
            h,m = map(int,horario.split(":"))
            return h * 60 + m
while True:
    try:
        entrada = input()
        chega = "8:00"

        if (para_minutos(entrada) + 60) > para_minutos(chega):
            saida = (para_minutos(entrada)+60)-para_minutos(chega)
            print("Atraso maximo:",saida)
        elif (para_minutos(entrada)+30)>para_minutos(chega):
            saida = (para_minutos(entrada)+30)-para_minutos(chega)
            print("Atraso maximo:",saida)
        else:
            print("Atraso maximo:",0)
    except EOFError:
        break
#cozinhei dms slk