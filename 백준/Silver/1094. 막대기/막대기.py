X = int(input())

stick = 64
st_list = []
cnt = 0

while X > 0 :
    if stick > X :
        stick = stick // 2
    else :
        cnt += 1
        X -= stick

print(cnt)