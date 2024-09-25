N, B = map(int, input().split())

# 진법 변환 결과를 담을 리스트
result = []

# 진법 변환
while N > 0:
    remainder = N % B
    result.append(remainder)
    N //= B

# 결과는 역순으로 계산되었으므로 뒤집기
result.reverse()

# 출력
for i in result:
    if i >= 10:
        print(chr(i + 55), end="")  # 10 이상인 경우 문자로 변환
    else:
        print(i, end="")  # 10 미만인 경우 그대로 출력