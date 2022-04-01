import sys

n = int(input())

for i in range(n):
    a = input()
    a_list = list(a)
    t = int(a_list[0])
    a_list = a_list[2:]
    ans = []
    
    for j in range(len(a_list)):
        for k in range(t):
            ans.append(a_list[j])
            
    answ = ''.join(ans)
    print(answ)
