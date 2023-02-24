a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
result_1 = (a + b) % c
result_2 = ((a % c) + (b % c)) % c
result_3 = (a * b) % c
result_4 = ((a % c) * (b % c)) % c
print(result_1)
print(result_2)
print(result_3)
print(result_4)