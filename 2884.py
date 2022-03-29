h, m = map(int, input().split())

if(m>=45):
    m = m - 45
elif(h>0):
    h = h - 1
    m = m + 15
else:
    h = 23
    m = m + 15

print(str(h) + " " + str(m))
