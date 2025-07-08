import sys

l = [True]*1000001

for i in range(2, int(len(l) ** 0.5) + 1):
    if l[i]:
        for j in range(i + i, len(l), i):
            l[j] = False

while True:
    n = int(sys.stdin.readline())
    tag = 0    
    
    if n == 0:
        break

    for i in range(3, n//2 + 1, 2):
        if l[i] and l[n - i]:
            print(f"{n} = {i} + {n - i}")
            tag = 1
            break
            
    if tag == 0:
        print("Goldbach's conjecture is wrong.")