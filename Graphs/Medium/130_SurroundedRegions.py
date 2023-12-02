class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        checkSec = set()
        def tempCheck(row, col):
            if((row, col) in checkSec or row < 0 or col < 0 or row >= ROWS or col >= COLS  or board[row][col] == "X"):
                return
            
            board[row][col] = "T" # temp flip
            checkSec.add((row, col))
            moves = [[1,0], [0,1], [-1,0], [0,-1]]
            for move in moves:
                tempCheck(row+move[0], col+move[1])
        
        # check temp starting from outer edge and working inwards to mark all O's as T for temp
        for row in range(ROWS):
            for col in range(COLS):
                if(row == 0 or col == 0 or row == ROWS-1 or col == COLS-1):
                    if(board[row][col] == "O"):
                        tempCheck(row, col)

        # move remaining O's to X's
        for row in range(ROWS):
            for col in range(COLS):
                if(board[row][col] == "O"):
                    board[row][col] = "X"

        # move previous checks back to O's
        for row in range(ROWS):
            for col in range(COLS):
                if(board[row][col] == "T"):
                    board[row][col] = "O"

