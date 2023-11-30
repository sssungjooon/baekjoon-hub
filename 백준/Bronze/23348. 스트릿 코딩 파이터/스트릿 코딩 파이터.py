# 첫째 줄에 세 가지 기술의 난이도 A, B, C
# 한손 - 노룩 - 폰
A, B, C = map(int,input().split())
# 참가한 동아리의 수 N
N = int(input())
# 각 동아리 별 합계 넣기
result = []

# 3N 줄에 걸친 동아리 기술 사용 정보 입력 받기
for _ in range(N):
    # 동아리 점수 초기화
    point = 0
    # 각 동아리의 3명의 점수 받기
    for i in range(3):
        a, b, c = map(int,input().split())
        P = a*A + b*B + c*C
        point += P
    # 3명의 점수를 받았으면 result로 옮기기
    result.append(point)
print(max(result))