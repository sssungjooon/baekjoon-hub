# 버블소트로 풀어보자
# 첫째 줄 학생 수
S = int(input())
number = list(map(int,input().split()))

# 줄을 선 학생 수 받을 리스트
student = []

# 학생 수 만큼 반복 (범위는 1부터 S까지)
for i in range(1,S+1):
    student.append(i)
    # 학생 한 명을 받으면 아까 받은 number 순서대로 버블소트
    # 단 숫자가 0이면 패스 (그대로 둔다)
    if number[i-1] == 0 :
        continue
    # 그 외의 경우에는 넣은 숫자를 number[i-1]번만큼 앞으로 땡기기
    else :
        #for _ in range(number[i-1]) :
        #    for k in range(len(number) - 1, 0, -1):
        for j in range(len(student)-1,len(student)-number[i-1]-1 ,-1) :
            student[j-1], student[j] = student[j], student[j-1]

print(*student)