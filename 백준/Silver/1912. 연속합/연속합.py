n = int(input())
answer = list(map(int,input().split()))

for i in range(1,n):
    answer[i] = max(answer[i],answer[i-1]+answer[i])
    
print(max(answer))