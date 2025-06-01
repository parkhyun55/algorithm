N = int(input())
s = str(input())
num = [0] * N
post_stack = []

for i in range(N):
    num[i] = int(input())
    
for i in s:
    if i.isalnum():
        post_stack.append(num[ord(i) - ord('A')])
    else:
        n2 = post_stack.pop()
        n1 = post_stack.pop()
        
        if i == '+':
            post_stack.append(n1 + n2)
            
        elif i == '-':
            post_stack.append(n1 - n2)
            
        elif i == '*':
            post_stack.append(n1 * n2)
            
        elif i == '/':
            post_stack.append(n1 / n2)
            
print('%.2f' %post_stack[0])