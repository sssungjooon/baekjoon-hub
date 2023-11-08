from collections import *
dr=[-1,1,0,0]
dc=[0,0,1,-1]
 
def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    q = deque()
    dist = [[987654321 for _ in range(M)] for _ in range(N)]
    
    # 로봇(R)의 시작 위치를 찾아 큐에 추가
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                q.append((i,j,0))
                dist[i][j] = 0
        if q:
            break
            
    while q:
        r,c,k = q.popleft()
        
        # 목표 지점(G)에 도착한 경우 이동 횟수 반환
        if board[r][c] == 'G':
            return k
        
        # 네 방향으로 이동할 수 있는 경우 탐색
        for i in range(4):
            nr = r
            nc = c
            
            # 해당 방향으로 미끄러지며 이동 가능한 위치 찾기
            while 0<=nr+dr[i]<N and 0<=nc+dc[i]<M and board[nr+dr[i]][nc+dc[i]] != 'D':
                nr += dr[i]
                nc += dc[i]
            
            # 이전에 해당 위치에 도달한 적이 없거나, 이전에 도달한 경우보다 적은 이동 횟수로 도달 가능한 경우
            if dist[nr][nc] > k+1:
                dist[nr][nc] = k+1
                q.append((nr,nc,k+1))
    
    # 목표 지점에 도착할 수 없는 경우 -1 반환
    return -1
