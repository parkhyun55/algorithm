a, b, c = map(int, input().split())
l = []
l.append(a)
l.append(b)
l.append(c)
l.sort(reverse=True)

if l[0] < l[1] + l[2]:
    print(sum(l))
else:
    l[0] = l[1] + l[2] - 1
    print(sum(l))