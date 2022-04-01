a = []
t = 0

for i in range(10):
    inp = int(input())
    inp = inp % 42
    a.append(inp)

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i] == a[j]):
            a[j] = -1

for i in range(len(a)):
    if(a[i] >= 0):
        t += 1
print(t)
