N, M = map(int, input().split())
list = [0] * N
tmp = 0
for i in range(N):
    list[i] = i + 1
for i in range(M):
    a, b = map(int, input().split())
    tmp = list[a - 1]
    list[a - 1] = list[b - 1]
    list[b - 1] = tmp
for i in list:
    print(i, end=" ")