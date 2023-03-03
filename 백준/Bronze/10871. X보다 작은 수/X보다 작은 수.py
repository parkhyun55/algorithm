N, X = map(int, input().split())
A = map(int, input().split())
A = list(A)
result = []

for i in A:
    if i < X:
        result.append(i)

for i in result:
    print(i, end = " ")