a, b, v = map(int, input().split())
x = int((v - a) / (a - b))
v1 = v - (a - b) * x
h = 0
while True:
    if(h < v1):
        h += a
        x += 1
    if(h < v1):
        h -= b
    else:
        print(x)
        break



