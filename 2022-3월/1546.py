import sys

n = int(input())
grade = input()

grade_list = grade.split()
grade_list = list(map(int, grade_list))
max = 0

for i in range(n):
    if(max < grade_list[i]):
        max = grade_list[i]

sum = sum(grade_list)
div = n * max
print(sum*100/div)
