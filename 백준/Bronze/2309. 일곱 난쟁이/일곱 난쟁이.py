from itertools import combinations

member = []
for _ in range(9):
    member.append(int(input()))

temp = list(combinations(member,7))

seven = []

for tem in temp :
    if not seven and sum(tem) == 100 :
        for t in tem :
            seven.append(int(t))

for ans in sorted(seven) :
    print(int(ans))