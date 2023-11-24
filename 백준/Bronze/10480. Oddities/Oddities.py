def check_odd_or_even(x):
    if x % 2 == 0:
        return f"{x} is even"
    else:
        return f"{x} is odd"

# 테스트 케이스의 개수 입력
n = int(input())

# 각 테스트 케이스에 대한 결과 출력
for _ in range(n):
    x = int(input())
    result = check_odd_or_even(x)
    print(result)
