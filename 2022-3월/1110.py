t = 0
n = input()
first = int(n)

while True:
    num = list(n)
    num = list(map(int, num))    
    sum_num = sum(num)

    right = sum_num % 10
    left = int(n) % 10

    new = 10 * left + right

    t += 1
    
    if(first == new):
        print(t)
        break
    else:
        n = str(new)





