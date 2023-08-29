N = int(input())
P = 2
for i in range(N):
    # 한 변의 점 개수
    P = P + (P-1)
result = P*P
print(result)