numbers = []
for _ in range(5):
    num = int(input())
    numbers.append(num)
ever = sum(numbers)//5
print(ever)

# 중앙값
mid = sorted(numbers)
print(mid[2])
