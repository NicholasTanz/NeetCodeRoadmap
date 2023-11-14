class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        
        # capturing all unsurronded regions (borders - then cover cells nxt to borders)
        def capture(r, c):
            # handles not in bounds & X's - don't capture 
            if(r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O"):
                return
            board[r][c] = "T"
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c+1)
            capture(r, c-1)

        # find unsurronded regions and capture them temporarliy. 
        for r in range(ROWS):
            for c in range(COLS):
                if(board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    capture(r, c)
        
        # capture all other regions of O's - we know are surronded
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # turn unsurronded regions back into O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
            

