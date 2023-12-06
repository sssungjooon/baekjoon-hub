# 관찰 횟수 입력
N = int(input())
observations = {}  # 소의 번호와 위치를 저장할 딕셔너리 초기화
cross_count = 0  # 길을 건넌 횟수 초기화

# N번의 관찰을 입력받고 처리
for _ in range(N):
    number, position = map(int, input().split())
    # 소의 번호가 이미 딕셔너리에 있고, 위치가 다르면 길을 건넌 것으로 카운트
    if number in observations and observations[number] != position:
        cross_count += 1
    observations[number] = position  # 현재 관찰 결과를 딕셔너리에 저장

# 길을 건넌 최소 횟수 출력
print(cross_count)