N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(i + 1)
temp = 0

for i in range(M):
    a, b = map(int, input().split())
    temp = A[a - 1]
    A[a - 1] = A[b - 1]
    A[b - 1] = temp

for i in A:
    print(i, end = ' ')