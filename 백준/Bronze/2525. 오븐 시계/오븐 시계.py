# 현재 시각 시 A, 분 B
A, B = map(int,input().split())
# 요리하는 데 필요한 시간
C = int(input())

time = [A, B]
plus = [C//60, C%60]
new_time = [A+ (C//60),0]

if B+ plus[1] >= 60 :
    new_time[0] += 1
    new_time[1] = B + plus[1] - 60
else :
    new_time[1] = time[1] + plus[1]

if new_time[0] >= 24 :
    new_time[0] -= 24

print(*new_time) 