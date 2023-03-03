N, M = list(map(int, input().split()))
A = []
temp = []

for i in range(N):
    A.append(i + 1)

for _ in range(M):
    i, j = map(int, input().split())
    A = A[0:i-1] + A[i-1:j][::-1] + A[j:]

for i in A:
    print(i, end = ' ')
