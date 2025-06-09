# 실패
repeat = int(input())
answer = []

for _ in range(repeat):
    d = int(input())
    patton = list(map(int, input().split()))
    before_piece = []
    cnt = 0
    for p in patton:
        if p in before_piece:
           cnt +=1
           before_piece = []
           before_piece.append(p)
        else:
            before_piece.append(p)
    if len(before_piece) > 0:
        cnt +=1
    answer.append(cnt) 


print(*answer)