import math

N, S = map(int, input().split())
A = list(map(int, input().split()))

for i in range(len(A)):
    A[i] = abs(S - A[i])

result = A[0]

for i in range(1, N):
    result = math.gcd(result, A[i])
    
print(result)