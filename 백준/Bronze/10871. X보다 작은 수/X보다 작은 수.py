N, X = map(int,input().split())
numbers = list(map(int,input().split()))
small = []
for num in numbers :
    if num < X :
        small.append(num)
print(*small)