numbers = []
for _ in range(9):
    K = int(input())
    numbers.append(K)
# 최대 값을 찾고
maxnum = max(numbers)
# 몇 번째인지 찾자
result = 0
for i in range(len(numbers)):
    if numbers[i] == maxnum :
        result = i+1
print(maxnum)
print(result)
