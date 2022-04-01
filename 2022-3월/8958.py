n = int(input())

for i in range(n):
    grade = 0
    sum = 0
    a = input()
    al = list(a)

    for j in range(len(a)):
        if(al[j] == 'O'):
            grade +=1
            sum += grade
        else:
            grade = 0
    print(sum)
