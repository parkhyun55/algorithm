list = [42] * 10
for i in range(10):
    n = int(input()) % 42
    if n not in list:
        list[i] = n
while 42 in list:
    list.remove(42)
print(len(list))