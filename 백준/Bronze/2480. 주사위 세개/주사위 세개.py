a, b, c = map(int, input().split())
if a == b and b != c:
    prise = 1000 + a * 100
elif b == c and c != a:
    prise = 1000 + b * 100
elif c == a and a != b:
    prise = 1000 + c * 100
elif a == b and b == c:
    prise = 10000 + a * 1000
else:
    if a > b and a > c:
        prise = 100 * a
    elif b > c and b > a:
        prise = 100 * b
    elif c > a and c > b:
        prise = 100 * c
print(prise)