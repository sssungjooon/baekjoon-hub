# 첫째 줄 총 금액 X
X = int(input())
# 둘째 줄 물건의 개수 N
N = int(input())
pricesum = 0
for thing in range(N):
    A, B = map(int,input().split())
    price = A * B
    pricesum += price

if X == pricesum :
    print('Yes')
elif X != pricesum :
    print('No')