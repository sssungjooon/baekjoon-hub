T = int(input())

for test_count in range(T):
    a, b = map(int,input().split())
    aa = a%10
    # 10 뒷자리가 0일 때 10 출력
    if aa == 0 :
        print(10)
    # 1, 5, 6, 10은 제곱해도 같다
    elif aa == 1 or aa == 5 or aa == 6 :
        print(aa)
    # 2일 때, 2, 4, 8, 6 반복
    elif aa == 2 :
        num2 = [2, 4, 8, 6]
        print(num2[b%4-1])
        
    # 3일 때, 3, 9, 7, 1 반복
    elif aa == 3 :
        num3 = [3, 9 ,7, 1]
        print(num3[b%4-1])

    # 4일 때, 4, 6 반복
    elif aa == 4 :
        num4 = [4, 6]
        print(num4[b%2-1])

    # 7일 때, 7, 9, 3, 1 반복
    elif aa == 7 :
        num7 = [7, 9, 3, 1]
        print(num7[b%4-1])

    # 8일 때, 8, 4, 2, 6 반복
    elif aa == 8 :
        num8 = [8, 4, 2, 6]
        print(num8[b%4-1])

    # 9일 때, 9, 1 반복
    elif aa == 9 :
        num9 = [9, 1]
        print(num9[b%2-1])