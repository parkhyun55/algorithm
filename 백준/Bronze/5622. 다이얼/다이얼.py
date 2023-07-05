dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s = input()
time = 0

for i in s:
    for j in dial:
        if i in j:
            time = time + dial.index(j) + 3
print(time)