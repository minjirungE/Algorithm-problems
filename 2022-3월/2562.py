max = 0

for i in range(9):
    a = int(input())
    if(max < a):
        max = a
        t = i+1

print(max)
print(t)
