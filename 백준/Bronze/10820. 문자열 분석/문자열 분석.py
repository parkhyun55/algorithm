while True:
    try:
        S = list(input())
        result = [0] * 4
        for i in S:
            if i == ' ':
                result[3] = result[3] + 1
            
            elif 97 <= ord(i) <= 122:
                result[0] = result[0] + 1
                
            elif 65 <= ord(i) <= 90:
                result[1] = result[1] + 1
        
            else:
                result[2] = result[2] + 1
        print(" ".join(map(str, result)))
        
    except EOFError:
        break