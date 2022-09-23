from itertools import combinations

# 카드의 개수 N, 점수 합이 M에 가까워야 한다.
N, M = map(int,input().split())
card = list(map(int,input().split()))
combi = list(combinations(card,3))
three_card = []
find_max = []

for com in combi :
    three_card.append(sum(com))

for three in three_card :
    if three > M :
        continue
    else :
        find_max.append(three)

print(max(find_max))