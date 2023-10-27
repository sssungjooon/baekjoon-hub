from itertools import combinations

N = int(input())
maxnums = []
for _ in range(N):
    check = []
    card = list(map(int,input().split()))
    numbers = list(combinations(card, 3))
    # print(numbers)
    for num in numbers :
        c = sum(num)%10
        check.append(c)
    maxnums.append(max(check))
# print(maxnums)
lastcheck = []
for i in range(len(maxnums)):
    if maxnums[i] == max(maxnums) :
        lastcheck.append(i+1)
print(max(lastcheck))