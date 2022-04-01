a = input()
al = list(a)

alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
pr = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

for i in range(len(al)-1, -1, -1):
    for j in range(26):
        if(al[i] == alp[j]):
            pr[j] = i

pr = list(map(str, pr))
ans = ' '.join(pr)
print(ans)
