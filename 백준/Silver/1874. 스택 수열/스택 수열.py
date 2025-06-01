n = int(input())
stack = []
result = []
flag = 0
cur = 1

for i in range(n):
    l = int(input())
    while cur <= l:
        stack.append(cur)
        result.append("+")
        cur = cur + 1

    if stack[-1] == l:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        flag = 1
        break
if flag == 0:
    for i in result:
        print(i)