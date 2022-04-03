n = int(input())
i = 1
t = 1
while True:
    if(t < n):
        t = t + 6 * i
        i += 1
    else:
        break

print(i)
