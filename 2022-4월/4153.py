while True:
    a = input()
    al = a.split()
    al = list(map(int, al))

    if(al[0]==0 and al[1]==0 and al[2]==0):
        break

    al.sort()

    if(al[0]*al[0] + al[1]*al[1] == al[2]*al[2]):
        print("right")
    else:
        print("wrong")
