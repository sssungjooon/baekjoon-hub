N, M = map(int,input().split())
price = []
pack_min = 9999999
piece_min = 9999999
# 6줄 패키지 가격 및 낱개 가격
for i in range(M):
    package, piece = map(int, input().split())
    if package < pack_min :
        pack_min = package
    if piece < piece_min :
        piece_min = piece

price.append((N//6)*pack_min + (N%6)*piece_min)
price.append(N*piece_min)
price.append((N//6 + 1) * pack_min)
# print(price)
result = min(price)
print(result)