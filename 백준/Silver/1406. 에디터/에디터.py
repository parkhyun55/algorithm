import sys

stack_l = list(sys.stdin.readline().strip())
stack_r = []
N = int(sys.stdin.readline())

for i in range(N):
    s_ = sys.stdin.readline().split()
    
    if s_[0] == 'L':
        if len(stack_l) != 0:
            stack_r.append(stack_l.pop())
        else: 
            continue
            
    elif s_[0] == 'D':
        if len(stack_r) != 0:
            stack_l.append(stack_r.pop())
        else: 
            continue
            
    elif s_[0] == 'B':
        if len(stack_l) != 0:
            stack_l.pop()
        else: 
            continue
            
    elif s_[0] == 'P':
        stack_l.append(s_[1])
        
answer = stack_l + stack_r[::-1]

print("".join(answer))