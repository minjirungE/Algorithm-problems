n = int(input())
a = input()
b = list(a)

alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(n):
    for j in range(26):
        if(b[i] == alp[j]):
            b[i] = j + 1

f = 0
for i in range(n):
    f += b[i] * (31 ** i)

print(f % 1234567891)

