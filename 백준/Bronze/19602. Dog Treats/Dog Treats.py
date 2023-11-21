# 입력 받기
S = int(input())
M = int(input())
L = int(input())

# 행복 점수 계산
happiness_score = 1 * S + 2 * M + 3 * L

# 결과 출력
if happiness_score >= 10:
    print("happy")
else:
    print("sad")
