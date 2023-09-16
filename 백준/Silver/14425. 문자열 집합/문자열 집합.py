N, M = map(int,input().split())
S = []
result = 0
# S에 포함되는 문자열
for _ in range(N):
    word = str(input())
    S.append(word)
# 검사해야하는 문자열
for _ in range(M):
    check = str(input())
    if check in S :
        result += 1
# 끝났다면 프린트
print(result)