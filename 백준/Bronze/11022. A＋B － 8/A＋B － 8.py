T = int(input())

for test_count in range(1,T+1):
    A, B = map(int,input().split())
    print(f'Case #{test_count}: {A} + {B} = {A+B}')