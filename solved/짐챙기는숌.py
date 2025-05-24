N, M = list(map(int, input().split()))

if N == 0 or M == 0:
    print("0")
else:
    book = list(map(int, input().split()))
    cnt = 0
    box = M
    for b in book:
        if b <= box:
            box -= b
            
        else:
            box = M
            box -= b
            cnt +=1
            
    if box is not M:
        cnt +=1
        print(cnt)
    else:
        print(cnt)