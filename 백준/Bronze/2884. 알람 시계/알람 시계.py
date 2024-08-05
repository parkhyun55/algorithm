hours, min = map(int, input().split())
if min < 45:
    if hours == 0:
        hours = hours + 23
        min = min + 15
    else :
        hours = hours - 1
        min = min + 15
else:
    min = min - 45
print(hours, min)