import math

def maximize_pizza(n, datasets):
    results = []
    
    for i in range(n):
        A1, P1 = datasets[i][0]
        R1, P2 = datasets[i][1]

        area_per_dollar_slice = A1 / P1
        area_per_dollar_whole = math.pi * (R1 ** 2) / P2

        if area_per_dollar_whole > area_per_dollar_slice:
            results.append("Whole pizza")
        else:
            results.append("Slice of pizza")

    return results

# 입력 받기
n = int(input())
datasets = []

for _ in range(n):
    A1, P1 = map(int, input().split())
    R1, P2 = map(int, input().split())
    datasets.append(((A1, P1), (R1, P2)))

# 결과 출력
results = maximize_pizza(n, datasets)
for result in results:
    print(result)
