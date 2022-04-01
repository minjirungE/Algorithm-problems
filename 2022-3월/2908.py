inp = input()
inp_list= inp.split()

a = inp_list[0]
a_list = list(a)
a_list.reverse()
a = int(''.join(a_list))

b = inp_list[1]
b_list = list(b)
b_list.reverse()
b = int(''.join(b_list))

if(a > b):
    print(a)
else:
    print(b)
