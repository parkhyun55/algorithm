N, M = map(int, input().split())
A = [0] * N

for i in range(M):
    a, b, c = map(int, input().split())
    for j in range(a - 1, b):
         A[j] = c

for i in A:
    print(i, end = ' ')