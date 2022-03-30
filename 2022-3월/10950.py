n = int(input())
list = []

for i in range(n):
    a, b = map(int, input().split())
    list.append(a+b)

for i in range(n):
    print(list)
    
