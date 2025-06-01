S = input()
count = [0] * 26

for i in S:
    count[ord(i) - 97] = count[ord(i) - 97] + 1
    
print(" ".join(map(str, count)))