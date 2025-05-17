N, M = list(map(int, input().split()))
firstWhite = []
firstBlack = []

for i in range(8):
    appendblack = []
    appendwhite = []
    for j in range(8):
        if (i + j) % 2:
            appendblack.append("B")
            appendwhite.append("W")
        else:
            appendblack.append("W")
            appendwhite.append("B")
    firstBlack.append(appendblack)
    firstWhite.append(appendwhite)      

grid = []
for h in range(N):
    grid.append([])
    b = input()
    for w in b:
        grid[h].append(w)

def checkBoard(board, black, white):
    check_h = N - 7
    check_w = M - 7

    mincnt = []
    for i in range(check_h):
        for j in range(check_w):
            cnt = [0, 0]
            for k in range(8):
                for b in range(8):
                    if board[i+k][j+b] != black[k][b]:
                        cnt[0] += 1
                    if board[i+k][j+b] != white[k][b]:
                        cnt[1] += 1
            mincnt.append(cnt[0])
            mincnt.append(cnt[1])
                     
    return min(mincnt)
print(checkBoard(grid, firstBlack, firstWhite))

"""N, M = map(int, input().split())
firstWhite = []
firstBlack = []

grid = []
for i in range(1, 9):
    firstBlack.append([])
    firstWhite.append([])
    if not i % 2:
        firstBlack[i-1].append("B")
        firstWhite[i-1].append("W")
    else:
        firstBlack[i-1].append("W")
        firstWhite[i-1].append("B")
    for j in range(0, 7):
        if firstBlack[i-1][-1] == "B":
            firstBlack[i-1].append("W")
        else:
            firstBlack[i-1].append("B")
        
        if firstWhite[i-1][-1] == "W":
            firstWhite[i-1].append("B")
        else:   
            firstWhite[i-1].append("W")
    
    

for i in range(N):
    grid.append([])
    k = input()
    for j in k:
        grid[i].append(str(j))

def boardCheck(black, white, board, wide, height):
    cnt = [0,0] # black, white순서 행 열판단해서 len(n) - 8 그리고 len(m) - 8한값으로 판단한다
    answer = []
    board = list(board)
    check_wide = wide - 8
    check_height = height - 8
    for i in range(check_wide):
        for j in range(check_height):
            for b in range(0, 8):
                for w in range(0, 8):
                    if board[b+i][w+j] != black[b][w]:
                        cnt[0] += 1
                    if board[b+i][w+j] != white[b][w]:
                        cnt[1] += 1
    
    answer.append(cnt[0])
    answer.append(cnt[1])

    return min(answer)
print(boardCheck(firstBlack, firstWhite, grid, N, M))

"""