T = int(input())

for t in range(T):
    stack = []
    vps = list(input())
    check = 0
    for v in vps :
        if v == "(" :
            check += 1
        elif v == ")" :
            check -= 1
        # check 가 음수이면 )가 먼저 나와서 짝이 안맞으므로
        if check < 0 :
            print("NO")
            break
    
    # "("만 있따면 check가 양수
    if check > 0 :
        print("NO")
    # check가 0이면 () 짝이 맞다는 것이므로
    elif check == 0 :
        print("YES")