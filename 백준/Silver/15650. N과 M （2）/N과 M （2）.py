from itertools import combinations

N, M = map(int,input().split())
num = [i for i in range(1,N+1)]
numbers = list(combinations(num,M))

for nums in numbers :
    print(*nums)