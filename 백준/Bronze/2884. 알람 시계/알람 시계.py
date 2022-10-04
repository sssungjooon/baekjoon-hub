H, M = map(int,input().split())

new_time = [H, M-45]

if new_time[1] < 0 :
    new_time[1] = 60 + new_time[1]
    new_time[0] -= 1
    if new_time[0] < 0 :
        new_time[0] = 24 + new_time[0]

print(*new_time)