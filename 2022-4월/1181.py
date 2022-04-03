import sys
dic = []
ch = []
while True:
    a = sys.stdin.readline()   
    if(a == '\n'):
        break #입력멈추기
    dic.append(a)

for i in range(len(dic)):# 숫자로 이루어진거 0으로 바꾸기 
    try:
        a = int(dic[i])
        ch.append(i)
    except:
        a = dic[i]

for i in range(len(ch)):
    dic[ch[i]] = 0

for i in range(len(dic)):# 단어가 같은거 0으로 바꾸기 
    for j in range(i+1, len(dic)):
        if(dic[i] == dic[j]):
            dic[j] = 0

l = dic.count(0)
for i in range(l):# 0인거 지우기
    dic.remove(0)

for i in range(len(dic)):# 리스트 요소를 리스트로 바꾸기 
    dic[i] = list(dic[i])
    dic[i].pop()

for i in range(len(dic)-1):# 리스트 요소 길이 비교해서 순서정하기(삽입정렬)
    for j in range(i+1, 0, -1):
        if(len(dic[j]) < len(dic[j-1])):
            dic[j], dic[j-1] = dic[j-1], dic[j]

for i in range(len(dic)-1):# 리스트 요소 알파벳 비교해서 순서정하기
    if(len(dic[i]) == len(dic[i+1])):
        
        for j in range((len(dic[i]))):
            if(ord(dic[i][j]) < ord(dic[i+1][j])):
                dic[i], dic[i+1] = dic[i+1], dic[i]

for i in range(len(dic)):# 리스트요소 다시 문자열로 붙이기
    dic[i] = ''.join(dic[i])
    print(dic[i])

