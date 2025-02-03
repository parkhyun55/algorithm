while True:
    a, b, c = map(int, input().split())

    l = []
    l.append(a)
    l.append(b)
    l.append(c)
    l.sort(reverse=True)

    if a == b == c:
        if a == 0:
            break
        else:
            print("Equilateral")
    
    elif l[0] >= l[1] + l[2]:
        print("Invalid")

    elif a == b or b == c or c == a:
        print("Isosceles")

    else:
        print("Scalene")