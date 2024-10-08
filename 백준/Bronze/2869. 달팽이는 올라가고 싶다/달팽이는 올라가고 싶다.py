A, B, V = map(int, input().split())
up = A - B
V -= B

if V % up == 0:
    print(V // up)
else:
    print((V // up) + 1)