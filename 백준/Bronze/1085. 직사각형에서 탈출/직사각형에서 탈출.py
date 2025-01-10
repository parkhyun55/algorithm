x, y, w, h = map(int, input().split())
diff = 1000

if abs(x - w) < diff:
    diff = abs(x - w)

if abs(y - h) < diff:
    diff = abs(y - h)

if abs(x - 0) < diff:
    diff = abs(x - 0)

if abs(y - 0) < diff:
    diff = abs(y - 0)

print(diff)