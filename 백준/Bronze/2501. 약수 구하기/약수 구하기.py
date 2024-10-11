N, K = map(int, input().split())
cnt = 0

for i in range(N):
    if N % (i + 1) == 0:
        cnt += 1

    if K == cnt:
        print(i + 1)
        break

    if N - 1 == i:
        print("0")