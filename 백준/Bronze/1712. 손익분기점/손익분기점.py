# A만원의 고정비용, B만원의 가변비용, 노트북 가격 C
A, B, C = map(int,input().split())

if B >= C:
    print(-1)
else:
    print(A//(C-B)+1)
