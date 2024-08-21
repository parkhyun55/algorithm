words = str(input()).upper()
words_ = list(set(words))
cnt = []
max_cnt = 0

for i in words_:
    cnt.append(words.count(i))

for i in cnt:
    if i > max_cnt:
        max_cnt = i

if cnt.count(max_cnt) > 1:
    print("?")
else:
    print(words_[cnt.index(max_cnt)])