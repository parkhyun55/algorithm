import sys

s = sys.stdin.readline()
s = s.replace('()', 'l')
index = 0
stack = []
result = 0

for i in s:
    if i == '(':
        stack.append(i)
        
    elif i == 'l' and len(stack) > 0:
        result = result + len(stack)
        
    elif i == ')' and len(stack) > 0:
        result = result + 1
        stack.pop()
        
print(result)