hour, min = input().split()
hour = int(hour)
min = int(min)
need_time = int(input())
hour_plus = (min + need_time) // 60

if hour_plus == 0:
    min = min + need_time
else:
    hour = hour + hour_plus
    min = min + need_time - 60 * hour_plus

if hour >= 24:
    hour = hour - 24

print(hour, min)