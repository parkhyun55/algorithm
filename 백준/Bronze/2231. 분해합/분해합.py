N = int(input())
M = "1"

while True:
    if N <= int(M):
        print(0)
        break

    l = []
    for i in M:
        l.append(int(i))

    M = int(M)
    if N == M + sum(l):
        print(M)
        break
    else:
        M = M + 1
        M = str(M)