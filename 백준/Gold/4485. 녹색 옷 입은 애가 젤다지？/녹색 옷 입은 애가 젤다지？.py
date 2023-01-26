import sys
import heapq

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
INF = sys.maxsize
tc = 1
while True:
    n = int(input())
    if n == 0:
        break
    #여기부터 각 케이스에 대한 알고리즘이다.
    board = [list(map(int, input().split())) for _ in range(n)]
    #q를 만들어 heapq로 만들어 잃은 돈을 기준으로 정렬되도록 한다.
    q = []
    heapq.heappush(q, (board[0][0], 0, 0)) # 잃은 돈, 좌표
    
    # 각 칸을 갈 때, 최소의 금액을 잃고 가도록 계속 갱신해준다.
    ans = [[INF for _ in range(n)] for _ in range(n)]
    ans[0][0] = board[0][0]
    result = 0
    
    while q:
        money, a, b = heapq.heappop(q)
        # 도착지점에 최소값을 저장한다.
        if a == n-1 and b == n-1:
            result = money
        # 4방향 다 갈수 있기 때문에 델타 탐색
        for ar in range(4):
            nr = a + dr[ar]
            nc = b + dc[ar]
            if 0<= nr < n and 0<= nc < n:
            	# 현재까지의 최소돈 + 다음지점돈 과 현재까지 계산된 다음지점의 잃은 돈 비교
                if money + board[nc][nr] < ans[nr][nc]:
                    ans[nr][nc] = money + board[nc][nr]
                    heapq.heappush(q, (money + board[nr][nc], nr, nc))
    print('Problem {}: {}'.format(tc, result))
    tc += 1