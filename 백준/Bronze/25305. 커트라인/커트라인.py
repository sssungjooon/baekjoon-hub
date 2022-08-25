# 첫째 줄에는 응시자의 수 N과 상을 받는 사람의 수 k가 공백을 사이에 두고 주어진다.
N, k = map(int,input().split())
score = list(map(int,input().split()))

# 버블 정렬로 순서 구현
for i in range(len(score) - 1, 0, -1):
        for j in range(0, i):
            if score[j] < score[j + 1]:
                score[j], score[j + 1] = score[j + 1], score[j]

# 인덱싱으로 프린트
print(score[k-1])