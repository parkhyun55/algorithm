N = int(input())
group_words = []
cnt = N

for i in range(N):
    group_words.append(str(input()))

for i in group_words:
    for j in range(len(i) - 1):
        if i[j] == i[j+1]:
            pass
        elif i[j] in i[j+1:]:
            cnt = cnt - 1
            break

print(cnt)