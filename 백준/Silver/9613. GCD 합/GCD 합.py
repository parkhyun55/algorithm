import sys
import math

t = int(sys.stdin.readline())


for i in range(t):
    n = list(map(int, sys.stdin.readline().split()))
    sum = 0
    for j in range(1, len(n)):
        for k in range(j + 1, len(n)):
            sum = sum + math.gcd(n[j], n[k])
        
    print(sum)