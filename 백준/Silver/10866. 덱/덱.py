import sys

N = int(input())
deque = []

for i in range(N):
    s = sys.stdin.readline().split()
    
    if s[0] == 'push_front':
        deque.insert(0, s[1])
        
    if s[0] == 'push_back':
        deque.append(s[1])
        
    if s[0] == 'pop_front':
        if len(deque) != 0:
            print(deque.pop(0))
        else:
            print(-1)
            
    if s[0] == 'pop_back':
        if len(deque) != 0:
            print(deque.pop())
        else:
            print(-1)
            
    if s[0] == 'size':
        print(len(deque))
        
    if s[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
            
    if s[0] == 'front':
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)
    
    if s[0] == 'back':
        if len(deque) != 0:
            print(deque[-1])
        else:
            print(-1)
    