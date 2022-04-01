a = input()
music = []
music = a.split()
music = list(map(int, music))

music_sort = [1,2,3,4,5,6,7,8]
music_rev = [8,7,6,5,4,3,2,1]

s = 0
r = 0

for i in range(8):
    if(music[i] == music_sort[i]):
        s += 1
    if(music[i] == music_rev[i]):
        r += 1

if(s == 8):
    print("ascending")
elif(r == 8):
    print("descending")
else:
    print("mixed")
