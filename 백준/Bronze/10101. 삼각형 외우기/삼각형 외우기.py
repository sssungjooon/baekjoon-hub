triangle = []
for _ in range(3):
    n = int(input())
    triangle.append(n)

if sum(triangle) != 180 :
    print('Error')
elif sum(triangle) == 180 :
    tri = set(triangle)
    if len(tri) == 1 :
        print('Equilateral')
    elif len(tri) == 2 :
        print('Isosceles')
    else :
        print('Scalene')