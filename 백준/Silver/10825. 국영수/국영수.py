# 도현이네 반의 학생의 수 N 인풋
N = int(input())
student = []
for _ in range(N) :
    # 학생 수만큼 인풋값을 리스트로 받는다.
    score = list(input().split())
    student.append(score)

# 람다 하나면 정렬 완료
# 첫번째로 국어 점수 내림차순
# 두번째로 영어 점수 오름차순
# 세번째로 수학 점수 내림차순
# 네번째로 모든 점수가 같으면 이름 오름차순
student.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 세트로 들어간 student 리스트 안의 값들을 이름만 차례대로 하나씩 뽑아내자
for i in student :
    print(i[0])