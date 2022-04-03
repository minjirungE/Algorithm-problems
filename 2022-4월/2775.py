def apartment(k, n):
    if(k == 0):
        return n
    else:
        sum = 0
        for i in range(n):
            sum += apartment(k-1, i+1)
        return sum

test = int(input())
for i in range(test):
    k = int(input())
    n = int(input())
    print(apartment(k, n))
