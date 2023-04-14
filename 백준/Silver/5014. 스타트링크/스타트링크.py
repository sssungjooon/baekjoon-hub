# 백준 5014번 스타트링크
from collections import deque

# 스타트링크 기업 면접날, 면접 건물에 늦게 도착한 강호
# 총 F층 고층 건물 사무실
# 스타트링크 있는 곳의 위치 G층
# 강호의 현재 위치 S층
# 엘레베이터를 타고 G층으로 이동하려는데, U버튼은 위로 U층을 가는 버튼, D버튼은 아래로 D층을 가는 버튼
# 강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램을 작성해라
# 만약, 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"를 출력

# 첫째줄에 F, S, G, U, D가 주어진다
# F = 총 층 / S = 현재 위치 / G = 목적지 층 / U = U버튼 누를 시 위로 가는 층 수 / D = D버튼 누를 시 아래로 가는 층 수
F, S, G, U, D = map(int,input().split())

# BFS 알고리즘을 사용하여 최소 버튼 수 계산
visited = [False] * (F+1)
q = deque([(S, 0)])  # 큐에 현재 층과 누른 버튼 수를 삽입
visited[S] = True
while q:
    floor, count = q.popleft()
    if floor == G :  # 목적지인 G층에 도착한 경우
        print(count)
        break
    if floor + U <= F and not visited[floor + U] :  # U 버튼을 누른 경우
        visited[floor + U] = True
        q.append((floor+U, count+1))
    if floor - D >= 1 and not visited[floor - D] :  # D 버튼을 누른 경우
        visited[floor - D] = True
        q.append((floor - D, count+1))
else:  # 목적지인 G층에 도착하지 못한 경우
    print("use the stairs")