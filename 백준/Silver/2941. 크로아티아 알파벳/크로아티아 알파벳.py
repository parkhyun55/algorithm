s = input()
s_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in s_list:
    s = s.replace(i, '!')
print(len(s))