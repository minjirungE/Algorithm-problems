a = int(input())
n = a
t = 0

while True:
    if(n >= 5):
        n = n - 5
        t += 1
    else:
        break
while True:
    if(n >= 3):
        n = n - 3
        t += 1
    else:
        break

if(n == 0):
    print(t)
else:
    t = 0
    while True:
        if(a >= 3):
            a = a - 3
            t += 1
        else:
            break
    if(a == 0):
        print(t)
    else:
        print(-1)
            
