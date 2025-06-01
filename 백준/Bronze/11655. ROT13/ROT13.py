S = str(input())
result = ""

for i in S:
    if 65 <= ord(i) <= 77:
        result = result + chr(ord(i) + 13)
        
    elif 78 <= ord(i) <= 90:
        result = result + chr(ord(i) - 13)
        
    elif 97 <= ord(i) <= 109:
        result = result + chr(ord(i) + 13)
        
    elif 110 <= ord(i) <= 122:
        result = result + chr(ord(i) - 13)
        
    else: 
        result = result + i
        
print(result)