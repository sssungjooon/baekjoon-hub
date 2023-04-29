# 백준 1931번 회의실 배정

N = int(input())
meetings = []

for i in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간 기준 오름차순, 시작 시간 기준 오름차순 정렬
end_time = 0  # 현재 회의가 끝나는 시간

count = 0  # 진행한 회의 수
for meeting in meetings:
    if meeting[0] >= end_time:  # 다음 회의가 현재 회의가 끝나는 시간보다 같거나 큰 경우
        end_time = meeting[1]  # 현재 회의 업데이트
        count += 1

print(count)  # 진행한 회의 수 출력

