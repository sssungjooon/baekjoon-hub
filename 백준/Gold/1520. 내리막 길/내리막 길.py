import sys
sys.setrecursionlimit(10**6)

M, N = map(int, input().split())
_map = []
for _ in range(M):
    _map.append(list(map(int, input().split())))

# dp 초기화
dp = [[-1] * N for _ in range(M)]

# (M-1, N-1) 지점은 목적지이므로 경로는 1개
dp[M-1][N-1] = 1

# 경로의 개수를 계산하는 함수
def dfs(x, y):
    if dp[x][y] != -1:  # 이미 계산된 경우
        return dp[x][y]

    dp[x][y] = 0  # 초기화

    if x > 0 and _map[x][y] > _map[x-1][y]:  # 위쪽으로 이동 가능한 경우
        dp[x][y] += dfs(x-1, y)
    if x < M-1 and _map[x][y] > _map[x+1][y]:  # 아래쪽으로 이동 가능한 경우
        dp[x][y] += dfs(x+1, y)
    if y > 0 and _map[x][y] > _map[x][y-1]:  # 왼쪽으로 이동 가능한 경우
        dp[x][y] += dfs(x, y-1)
    if y < N-1 and _map[x][y] > _map[x][y+1]: 
        dp[x][y] += dfs(x, y+1)

    return dp[x][y]

print(dfs(0, 0))

