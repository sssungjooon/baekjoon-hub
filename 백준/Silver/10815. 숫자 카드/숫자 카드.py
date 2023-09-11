N = int(input())
have = set(list(map(int,input().split())))
M = int(input())
check = list(map(int,input().split()))
result = []
for c in check :
    if c in have :
        result.append(1)
    else :
        result.append(0)
print(*result)