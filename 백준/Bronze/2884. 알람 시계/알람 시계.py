hour, min = input().split()
hour = int(hour)
min = int(min)

if min < 45:
    if hour == 0:
        hour = hour + 23
        min = min + 60
    else:
        hour = hour - 1
        min = min + 60

min = min - 45
print(hour, min)