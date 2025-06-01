import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    q = sys.stdin.readline().split()
    if q[0] == 'push':
        stack.append(q[1])
        
    elif q[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    
    elif q[0] == 'size':
        print(len(stack))
    
    elif q[0] == 'empty':
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    
    elif q[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])