N, B = input().split()
N = str(N)
B = int(B)
result = 0

for i in range(len(N)):
    pow = len(N) - i - 1
    
    if '0' <= N[i] <= '9':
        result += (B**pow) * (int(N[i]))
    else:
        result += (B**pow) * (int(ord(N[i])) - 55)

print(result)