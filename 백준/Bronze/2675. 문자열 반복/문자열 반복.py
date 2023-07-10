# 테스트케이스 개수 T
T = int(input())
for t in range(T):
    R, S = map(str, input().split())
    result = ''
    for s in S :
        result += s * int(R)
    print(result)