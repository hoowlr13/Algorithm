t = int(input())
for _ in range(t):
    door, button = list(map(int, input().split()))
    doorList = list(map(int, input().split()))
    doorcheck = False
    butcnt = False
    for d in doorList:
        if button <= 0 and d == 1:
            print("NO")
            butcnt = True
            break
        if d == 1 and not doorcheck:
            doorcheck = True
        if doorcheck:
            button -=1
    if not butcnt:
        print("YES")
        