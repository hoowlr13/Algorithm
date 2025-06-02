N = int(input())
wood = sorted(map(int, input().split()), reverse= True)
dayCnt = 1 # 나무를 사온 첫날이 1일
maxDay = 0
for w in wood:
    dayCnt +=1
    if not maxDay:
        maxDay = w + dayCnt
    else:
        if maxDay < (w + dayCnt):
            maxDay = (w + dayCnt)
print(maxDay)    