n = int(input())
print(' ' * (n - 1) + '*')
for i in range(1, n):
    print(' ' * (n - i - 1) + '*' + ' ' * (i * 2 - 1) + '*')