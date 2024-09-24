ary = [[0 for i in range(100)] for i in range((100))]
N = int(input())
sum = 0

for _ in range(N):
    x, y = map(int, input().split())
    
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            ary[i][j] = 1

for i in ary:
    sum += i.count(1)

print(sum)