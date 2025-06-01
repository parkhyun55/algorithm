N = int(input())
cnt = 0 #몇번째 종말의 수인지를 비교하기 위한 변수
N_ = 0 #종말의 수인지를 확인하기 위한 변수

while True:
    if "666" in str(N_):
        cnt = cnt + 1
        
    if N == cnt:
        break
    
    N_ = N_ + 1
    
print(N_)
        