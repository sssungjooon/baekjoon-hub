# 티 타입 입력
actual_tea_type = int(input())

# 참가자들의 답 입력
answers = list(map(int, input().split()))

# 정답 수 계산
correct_answers = answers.count(actual_tea_type)

# 정답 수 출력
print(correct_answers)
