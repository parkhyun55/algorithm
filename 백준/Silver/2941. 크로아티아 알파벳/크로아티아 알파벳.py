words = str(input())
croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0

for i in croa:
    words = words.replace(i, "*")

print(len(words))