n = int(input())
a = input()
al = list(a)
al = list(map(int, al))
sum = 0

for i in range(n):
    sum += al[i]
print(sum)
