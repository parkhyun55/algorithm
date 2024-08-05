hours, min = map(int, input().split())
need_time = int(input())
if (min + need_time) // 60 > 0:
    hours = hours + (min + need_time) // 60
    min = (min + need_time) % 60
else:
    min = min + need_time
if hours >= 24:
    hours = hours - 24
print(hours, min)