N = int(input())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

sorted_A = sorted(A_list, reverse=True)
sorted_B = sorted(B_list)

s = 0
for i in range(N) :
    s += sorted_A[i] * sorted_B[i]

print(s)