N, M = map(int, input().split())
list = [0] * (N)
for i in range(M):
    a, b, c = map(int, input().split())
    for j in range(a - 1, b):
        list[j] = c
for i in list:
    print(i, end=" ")