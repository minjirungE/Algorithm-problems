m, n = map(int, input().split())

array = [[0 for i in range(n)]for j in range(m)]

print(array)
for i in range(m):
    a = input()
    b = a.split()
    print(b)
    for j in range(n):
        array[i][j] = b[j]

print(array)
