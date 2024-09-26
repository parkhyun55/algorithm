T = int(input())
C = []

for i in range(T):
    c = int(input())
    C.append(c)

for i in C:
    q = int(i // 25)
    d = int((i % 25) // 10)
    n = int(((i % 25) % 10) // 5)
    p = int((((i % 25) % 10) % 5) // 1)
    print(q, d, n, p, end=" ")
    print()