while True:
    t = 0
    inp = input()
    if(int(inp) == 0):
        break
    
    a = list(inp)
    b = []
    
    for i in range(len(a)-1, -1, -1):
        b.append(a[i])

    for i in range(len(a)):
        if(int(a[i]) == int(b[i])):
            t += 1
            
    if(t == len(a)):
        print("yes")
    else:
        print("no")
