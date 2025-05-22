# 뭐가 문제인지 모르겠음
N, M = list(map(int, input().split()))

if N == 0 or M == 0:
    print("0")
else:
    # 해야될 동작? 
    # 1. 책을 박스에 집어넣는다
    # 2. 다음책을 집어넣는다
    # 2-1. 박스보다 작다면 집어넣는다
    # 2-2. 박스보다 크다면 책 cnt를 +1하고 새로운 박스에 담는다
    # 3. 만약 남은 책이없다면
    # 3-1. 박스에 담겨있는 책이 있다면 +1한다
    # 3-2. 박스에 담겨있는 책이 없다면 아무것도 하지않는다
    # 4. 책cnt를 출력한다
    book = list(map(int, input().split()))
    book.sort(reverse=True)
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