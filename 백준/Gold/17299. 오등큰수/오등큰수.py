def solution(nums):
    n = len(nums)
    result = [-1] * n  # 초기값으로 -1을 설정
    freq = {}  # 각 숫자의 등장 횟수를 저장하는 딕셔너리

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    stack = []  # 스택을 사용하여 현재 원소보다 작은 원소들의 인덱스를 저장

    for i in range(n):
        while stack and freq[nums[i]] > freq[nums[stack[-1]]]:
            result[stack.pop()] = nums[i]
        stack.append(i)

    return result

# 입력 받기
n = int(input())
nums = list(map(int, input().split()))

# 결과 출력
answer = solution(nums)
print(" ".join(map(str, answer)))
