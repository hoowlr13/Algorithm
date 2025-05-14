# 2025-05-14
N, M = input().split()
def verse_Sum(X, Y):

    verse_X = int(X[::-1])
    verse_Y = int(Y[::-1])
    verse_XY = str((verse_X+verse_Y))[::-1]
    return int(verse_XY)
    
print(verse_Sum(N, M))