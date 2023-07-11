# 총 다섯줄의 입력
words = []
length = []
for _ in range(5):
    temp = str(input())
    words.append(temp)
    length.append(len(temp))

result = ''

for i in range(max(length)) :
    for j in range(5):
        if i < length[j]:
            result += words[j][i]

print(result)