a = input()
a_list = a.split()
a_list = list(map(int, a_list))
sum = 0

for i in range(5):
    sum += a_list[i] * a_list[i]

print(sum%10)
