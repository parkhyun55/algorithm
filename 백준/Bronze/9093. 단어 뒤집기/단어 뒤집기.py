import sys

T = int(sys.stdin.readline())

for i in range(T):
    s = sys.stdin.readline().split()
    for j in s:
        print(j[::-1], end=' ')