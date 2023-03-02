X = int(input())
N = int(input())
money = 0

for i in range(N):
    a, b = input().split()
    a = int(a)
    b = int(b)
    money += a * b

if X == money:
    print('Yes')
else:
    print('No')