numbers = list(map(int,input().split()))
S = 0
for num in numbers :
    S += num**2
result = S%10
print(result)