N = int(input())
A = set(list(map(int,input().split())))
M = int(input())
numbers = list(map(int,input().split()))

for num in numbers :
    if num in A :
        print(1)
    else : 
        print(0)
