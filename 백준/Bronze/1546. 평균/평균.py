N = int(input())
score = input().split()

for i in range(N):
    score[i] = int(score[i])

M = max(score)
sum = 0

for i in range(N):
    sum = sum + score[i] * 100 / M
print(sum / N)