while True:
    R = int(input())
    if R == 0:
        break
    for i in range(0,R):
        for j in range(0,R):

            if i<R-i-1:
                distL = i
            else:
                distL = R-i-1

            if j<R-j-1:
                distC = j
            else:
                distC = R-j-1
            if distL < distC:
                dist = distL
            else:
                dist = distC
            print("%3d"%(dist+1),end="")
            if( j!= R-1):
                print(end=" ")

        print()
    print()