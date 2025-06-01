import sys
from collections import Counter

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * N
stack = []

freq = Counter(A)

stack.append(0)
for i in range(1, N):
    while stack and freq[A[stack[-1]]] < freq[A[i]]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)