N = int(input())
box = 0

while N >= 0:
    if N % 5 == 0:
        box = box + (N // 5)
        print(box)
        break
    N = N - 3
    box = box + 1
else:
    print("-1")
