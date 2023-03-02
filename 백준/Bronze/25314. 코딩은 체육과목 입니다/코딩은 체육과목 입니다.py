N = int(input())
long = N // 4
result = ''

for i in range(long):
    result += 'long '

result += 'int'
print(result)