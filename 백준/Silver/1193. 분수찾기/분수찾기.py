X = int(input())
line = 1

while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    d = X
    m = line - X + 1
    
else:
    d = line - X + 1
    m = X

print(str(d) + "/" + str(m))