A = []
count = 0

for i in range(10):
    a = int(input())
    b = a % 42
    if b not in A:
        A.append(b)

print(len(A))