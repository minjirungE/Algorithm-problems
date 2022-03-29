a, b, c = map(int, input().split())

print((a+b)%c)
#a와 b를 더하여 c로 나눈 나머지

print(((a%c)+(b%c))%c)
#a를 c로 나눈 나머지와 b를 c로 나눈 나머지를 더하여 c로 다시 나눈 나머지

print((a*b)%c)
#a와 b를 곱하여 c로 나눈 나머지

print(((a%c)*(b%c))%c)
#a를 c로 나눈 나머지와 b를 c로 나눈 나머지를 곱하여 c로 나눈 나머지
