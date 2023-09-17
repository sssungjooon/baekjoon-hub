# 로그에 기록된 출입 기록의 수 N
N = int(input())
# 회사 company
company = {}
for _ in range(N):
    A, B = map(str,input().split())
    if B == 'enter' :
        company[A] = 'enter'
    else:
        if company[A] :
            del company[A]
# 사전 순의 역순으로 한줄에 한명씩 출력
for member in sorted(company, reverse=True) :
    print(member)