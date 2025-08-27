class chess:
    def __init__(self, first_king_pos, first_stone_pos) -> str:
        self.king_pos = first_king_pos
        self.stone_pos = first_stone_pos
        self.board = [[chr(i) for i in range(ord('a'), ord('h')+1)] for _ in range(8)] 
        

    # def king(self, command) -> str:
    #     if command == 'R':
    #         if (self.king_pos + 1)  <= 8: 
    #         self.board()
    #     # elif command == 'L':
    #     # 
    
    # # def chessboard(self, board):ㅇ가나다
    #     # for i in range()


        




if __name__ == "__main__":
    A, B, C = list(map(str, input().split()))
    chessGame = chess(A, B)
    for i in range(C):
        key = input()
        chessGame.king(key)

    