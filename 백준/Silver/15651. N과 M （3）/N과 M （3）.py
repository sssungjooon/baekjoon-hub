from itertools import product

N, M = map(int,input().split())
num = [i for i in range(1,N+1)]
numbers = list(product(num,repeat=M))

for nums in numbers :
    print(*nums)