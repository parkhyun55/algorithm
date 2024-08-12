list = []
N, M = map(int, input().split())
for i in range(N):
    list.append(i+1)
for k in range(M):
    i, j = map(int, input().split())
    list = list[:i-1] + list[i-1:j][::-1] + list[j:]
for i in list:
    print(i, end=" ")