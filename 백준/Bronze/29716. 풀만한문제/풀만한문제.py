def count_harvestable_problems(J, N, problems):
    count = 0
    for problem in problems:
        size = 0
        for char in problem:
            if char.isupper():
                size += 4
            elif char.islower() or char.isdigit():
                size += 2
            elif char.isspace():
                size += 1

        if size <= J:
            count += 1

    return count

# 입력 받기
J, N = map(int, input().split())
problems = [input().strip() for _ in range(N)]

# 결과 출력
print(count_harvestable_problems(J, N, problems))
