class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        checkSec = set()
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        def markIsland(row, col):
            if(row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in checkSec or grid[row][col] == '0'):
                return

            checkSec.add((row, col))
            moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for move in moves:
                markIsland(row+move[0], col+move[1])                 

        for row in range(ROWS):
            for col in range(COLS):
                if((row, col) not in checkSec):
                    if(grid[row][col] == "1"):
                        markIsland(row, col)
                        islands += 1

        return islands
