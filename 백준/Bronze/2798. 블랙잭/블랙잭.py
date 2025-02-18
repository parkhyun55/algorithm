N, M = map(int, input().split())
l = list(map(int, input().split()))
sum = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if l[i] + l[j] + l[k] <= M and sum < l[i] + l[j] + l[k]:
                sum = l[i] + l[j] + l[k]
            else: 
                continue
print(sum)