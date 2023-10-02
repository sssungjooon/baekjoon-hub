N = int(input())
X = []
Y = []
result = 0
for _ in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
if N == 1 :
    result = 0
else :
    result = (max(X)-min(X))*(max(Y)-min(Y))

print(result)