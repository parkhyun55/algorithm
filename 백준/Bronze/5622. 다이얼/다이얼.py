word = str(input())
num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for i in word:
    for j in range(len(num)):
        if i in num[j]:
            time = time + j + 3
print(time)