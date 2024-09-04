l = []
max = 0
index_i = 0
index_j = 0

for i in range(9):
    l_ = list(map(int, input().split()))
    l.append(l_)

for i in range(9):
    for j in range(9):
        if l[i][j] >= max:
            max = l[i][j]
            index_i = i + 1
            index_j = j + 1

print(max)
print(index_i, index_j)