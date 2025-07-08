N = int(input())
pac = 1

if pac != 0:
    for i in range(1, N+1):
        pac = pac * i
        
pactorial = str(pac)[::-1]
cnt = 0

for i in pactorial:
    if i == '0':
        cnt = cnt + 1
    else:
        break
        
print(cnt)