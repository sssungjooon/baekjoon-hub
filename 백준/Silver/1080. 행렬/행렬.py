N, M = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(N)]
B = [list(map(int, list(input()))) for _ in range(N)]
cnt = 0

def check():
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return False
    return True

def solve(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]  # 뒤집기

for i in range(0, N-2):  # 0 ~ N-3
    for j in range(0, M-2):  # 0 ~ M-3
        if A[i][j] != B[i][j]:
            cnt += 1
            solve(i, j)

if check():
    print(cnt)
else:
    print(-1)