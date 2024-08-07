N = int(input())
cnt = 0
list = input().split(" ")
v = int(input())
for i in list:
    if int(i) == v:
        cnt = cnt + 1
print(cnt)