x = int(input())
idx = 1    
puang = False

while(1) :
    x -= idx
    idx += 1
    puang = not puang
    if x < 0 :
        if puang :
            print(abs(x))
        else :
            print(0)
        break