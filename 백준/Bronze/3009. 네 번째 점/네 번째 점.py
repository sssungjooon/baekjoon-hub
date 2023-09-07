xpoint = []
ypoint = []
for _ in range(3):
    x, y = map(int,input().split())
    xpoint.append(x)
    ypoint.append(y)
for x in xpoint :
    if xpoint.count(x) == 1 :
        resultx = x
for y in ypoint :
    if ypoint.count(y) == 1 :
        resulty = y

print(resultx, resulty)