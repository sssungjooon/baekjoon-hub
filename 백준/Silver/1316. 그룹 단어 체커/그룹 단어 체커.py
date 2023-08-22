N = int(input())
result = 0
for _ in range(N):
    group = []
    check = 0
    word = str(input())
    for w in word :
        # 기존 그룹 내에 w가 없다면 넣기
        if w not in group :
            group.append(w)
            check += 1
        else :
            # 그룹 안에 있다면 바로 앞전의 단어가 같다면 체크
            if group[-1] == w :
                check += 1
    if check == len(word) :
        result += 1
print(result)