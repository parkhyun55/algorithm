l = []
column = 0
result = ""

## 가장 긴 column 구하기
for i in range(5):
    l_ = list(str(input()))
    l.append(l_)
    
    if len(l_) > column:
        column = len(l_)

## 전체 단어 길이 통일시키기
for i in range(5):
    if len(l[i]) != column:
        for j in range(column - len(l[i])):
            l[i].append('*')

## 세로로 이어붙이기
for i in range(column):
    for j in range(5):
        if l[j][i] == '*':
            pass
        else:
            result = result + l[j][i]
            
print(result)