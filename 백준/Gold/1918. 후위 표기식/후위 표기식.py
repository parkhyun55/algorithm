infix = str(input())
stack = []
result = ''

for i in infix:
    if i == '(':
        stack.append(i)
    
    elif i == ')':
        while stack and stack[-1] != '(':
            result = result + stack.pop()
        stack.pop()
        
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            result = result + stack.pop()
        stack.append(i)
        
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            result = result + stack.pop()
        stack.append(i)
    
    else:
        result = result + i
        
while stack:
    result = result + stack.pop()
print(result)
    