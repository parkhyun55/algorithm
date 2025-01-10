N = int(input())
d = 2
result = []

if N == 1:
    print()

while N > 1:
    if N % d == 0:
        result.append(d)
        N = N//d
        d = 2
    else:
        d = d + 1

for i in result:
    print(i)