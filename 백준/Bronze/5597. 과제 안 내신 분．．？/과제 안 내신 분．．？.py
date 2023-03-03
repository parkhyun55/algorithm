A = []
result = []

for i in range(28):
    a = int(input())
    A.append(a)

for i in range(1, 31):
    if i not in A:
        result.append(i)

print(result[0])
print(result[1])