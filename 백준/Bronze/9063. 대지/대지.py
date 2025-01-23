N = int(input())
x = []
y = []

for i in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

result_x = max(x) - min(x)
result_y = max(y) - min(y)

print(result_x * result_y)