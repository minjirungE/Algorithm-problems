a = input()
A = a.upper()
Al = list(A)
Alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Alp_= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(len(Al)):
    for j in range(26):
        if(Al[i] == Alp[j]):
            Alp_[j] += 1

ma = max(Alp_)
t = 0

for i in range(26):
    if( ma == Alp_[i] ):
        t += 1
        max = i

if(t == 1):
    print(Alp[max])
else:
    print("?")
