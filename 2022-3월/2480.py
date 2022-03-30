a, b, c = map(int, input().split())

if(a == b):
    if(b == c):
        print(10000 + 1000 * a)
    else:
        print(1000 + 100 * a)
elif(b == c):
    print(1000 + 100 * b)
elif(a == c):
    print(1000 + 100 * a)
else:
    if(a > b):
        if(a > c):
            print(a * 100)
        else:
            print(c * 100)
    else:
        if(b > c):
            print(b * 100)
        else:
            print(c * 100)
        
