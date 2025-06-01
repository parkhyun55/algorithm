import sys

T = int(input())

for i in range(T):
    stack = []
    vps = str(sys.stdin.readline())
    for j in vps:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack) == 0:
                print("NO")
                break
            else:
                stack.pop()
    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")