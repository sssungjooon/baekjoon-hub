N = int(input())
Class = list(map(int,input().split()))
result = 0
for i in range(1,len(Class)+1):
    if Class[i-1] != i :
        result += 1
print(result)