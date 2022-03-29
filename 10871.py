import sys

n, x = map(int, input().split())
hi = input()
hi_list = list(hi.split())
ans_list=[]

for i in range(n):
    if(int(hi_list[i]) < x):
        ans_list.append(hi_list[i])

ans = ' '.join(ans_list)
print(ans)

