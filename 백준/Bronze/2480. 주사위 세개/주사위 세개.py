A, B, C = map(int,input().split())

result = 0

if A == B and B == C and C == A :
    result = 10000 + A * 1000
elif A == B and B != C :
    result = 1000 + A * 100
elif B == C and B != A :
    result = 1000 + B * 100
elif C == A and B != A :
    result = 1000 + C * 100
elif A != B and B != C and C != A :
    result = max(A, B, C) * 100

print(result) 