a = int(input())
b = int(input())
c = int(input())

ans = str(a*b*c)
ans_list = list(ans)
ans_list = list(map(int, ans_list))
num_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for j in range(len(ans_list)):
    for i in range(10):
        if(ans_list[j] == i):
            num_list[i] += 1
            break

for i in range(10):
    print(num_list[i])
            
    
