n = int(input())
a = input()
al = a.split()
al = list(map(int, al))

min = min(al)
max = max(al)

print(str(min) + " " + str(max))
