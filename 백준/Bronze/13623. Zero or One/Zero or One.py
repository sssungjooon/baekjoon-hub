def zerinho_winner(A, B, C):
    if A != B and A != C:
        return 'A'
    elif B != A and B != C:
        return 'B'
    elif C != A and C != B:
        return 'C'
    else:
        return '*'

# 입력 받기
A, B, C = map(int, input().split())

# 결과 출력
print(zerinho_winner(A, B, C))
