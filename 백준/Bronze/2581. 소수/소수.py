M = int(input())
N = int(input())
sum = 0
min = N + 1

for i in range(M, N+1):
    for j in range(2, i+1):
        if i % j == 0:
            if j == i:
                sum = sum + i
                if min > i:
                    min = i
            break
if sum != 0:
    print(sum)
    print(min)
else:
    print("-1")