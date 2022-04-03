n, m = map(int, input().split())
c = input()
card = c.split()
card = list(map(int, card))
sum_list = []
sum = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = card[i] + card[j] + card[k]
            if(sum <= m):
                sum_list.append(sum)
ans = max(sum_list)
print(ans)
