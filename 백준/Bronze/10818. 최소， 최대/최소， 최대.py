N = int(input())
A = map(int, input().split())
A = list(A)
min = A[0]
max = A[0]

for i in A:
    if min > i:
        min = i
    if max < i:
        max = i

print(min, max)