T = int(input())
for _ in range(T):
    C = int(input())
    cent = C
    q, d, n, p = 0, 0, 0, 0
    q = cent//25
    cent = cent%25
    d = cent//10
    cent = cent%10
    n = cent//5
    cent = cent%5
    p= cent
    print(q, d, n, p)