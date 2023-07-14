from itertools import permutations

N, M = map(int,input().split())
num = [i for i in range(1,N+1)]
numbers = list(permutations(num,M))

for nums in numbers :
    print(*nums)