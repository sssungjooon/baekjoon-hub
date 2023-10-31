while True:
    N = int(input())
    if N == 0 :
        break
    else :
        result = 0
        for i in range(1,N+1):
            double = (N-i+1)**2
            result += double
        print(result)