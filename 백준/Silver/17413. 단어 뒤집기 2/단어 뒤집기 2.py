import sys

S = list(sys.stdin.readline().rstrip())
index = 0
start = 0

while index < len(S):
    if S[index] == '<':
        index = index + 1
        while S[index] != '>':
            index = index + 1
        index = index + 1
        
    elif S[index].isalnum():
        start = index
        while index < len(S) and S[index].isalnum():
            index = index + 1
        tmp = S[start:index]
        tmp.reverse()
        S[start:index] = tmp
    else:
        index = index + 1
        
print("".join(S))