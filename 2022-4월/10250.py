t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    room = int(n / h)
    floor = n % h
    
    if(floor == 0):
        floor = h
    else:
        room = room + 1
        
    if(room < 10):
        room = '0' + str(room)
    else:
        room = str(room)
        
    print(str(floor) + room)
