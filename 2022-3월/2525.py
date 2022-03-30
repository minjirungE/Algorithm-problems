h, m = map(int, input().split())
time = int(input())

m = m + time

if(m < 60):
    print(str(h) + " " + str(m))
else:
    while(m >= 60):
        m = m - 60
        h = h + 1
    if(h>=24):
        h = h - 24
    print(str(h) + " " + str(m))
