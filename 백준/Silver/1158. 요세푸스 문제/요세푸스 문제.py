N, K = map(int, input().split())
stack = [i for i in range(1, N + 1)]
result = []
num = 0

for i in range(N):
    num = num + K - 1
    if num >= len(stack):
        num = num%len(stack)
        
    result.append(str(stack.pop(num)))
        
print("<", ", ".join(result)[:], ">", sep='')