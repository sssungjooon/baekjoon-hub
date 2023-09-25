from itertools import combinations_with_replacement

N, M = map(int,input().split())
num = [i for i in range(1,N+1)]
numbers = list(combinations_with_replacement(num,M))

for nums in numbers :
    print(*nums)