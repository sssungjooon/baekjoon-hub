def p_first(n):
    for i in range(n):
        print('@'*n+' '*3*n+'@'*n)
 
def p_second(n):
    for i in range(n):
        print('@' * n + ' ' * 2 * n + '@' * n)
 
def p_mid(n):
    for i in range(n):
        print('@' * 3*n)
 
def sol(n):
    p_first(n)
    p_second(n)
    p_mid(n)
    p_second(n)
    p_first(n)
 
sol(int(input()))