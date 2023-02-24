a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
money = 0

if a == b and b == c:
    money = 10000 + a * 1000
else:
    if a != b and b != c and c != a:
        if a >= b and a >= c:
            money = a * 100
        else:
            if b >= c and b >= a:
                money = b * 100
            else:
                if c >= a and c >= b:
                    money = c * 100
    else:
        if a == b and b != c:
            money = 1000 + a * 100
        else:
            if b == c and c != a:
                money = 1000 + b * 100
            else:
                if c == a and a != b:
                    money = 1000 + c * 100

print(money)