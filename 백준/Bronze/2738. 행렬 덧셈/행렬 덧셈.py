N,M = map(int,input().split())
first = []
second = []

for _ in range(N):
    temp = list(map(int,input().split()))
    first.append(temp)

for _ in range(N):
    temp2 = list(map(int,input().split()))
    second.append(temp2)

for i in range(N):
    for j in range(M):
        first[i][j] += second[i][j]

for i in range(N):
    result = first[i]
    print(*result)