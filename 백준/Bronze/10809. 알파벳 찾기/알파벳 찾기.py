S = str(input())
alphabet_list = 'abcdefghijklmnopqrstuvwxyz'
# 처음 등장하는 위치 기록할 리스트
when_first = [-1]*len(alphabet_list)

for a in range(len(alphabet_list)) :
    for i in range(len(S)):
        if when_first[a] != -1 :
            break
        else :
            if alphabet_list[a] == S[i] :
                when_first[a] = i

print(*when_first)