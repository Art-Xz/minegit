count = 0
while True:
    try:
        sub = input()
        seq = input()
        qtd = 0
        lista = []
        count+=1
        pos = 0
        index = -1
        while True:
            pos = seq.find(sub,pos)
            if pos == -1:
                break
            qtd +=1
            index = pos
            pos+=1
            
            
        if qtd == 0:
            print(f"Caso #{count}:\nNao existe subsequencia")
            print()
        else:
            print(f"Caso #{count}:\nQtd.Subsequencias: {qtd}\nPos: {index+1}")
            print()
    except EOFError:
        break