N = int(input())
score = []
sum = 0

a = list(map(int, input().split()))

for i in range(N):
    score.append(a[i] / max(a) * 100)
    sum += score[i]

print(sum / N)