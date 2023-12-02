class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        checkSec = set()
        maxArea = 0
        
        def islandArea(row, col):
            if ((row, col) in checkSec or row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0):
                return 0
            
            area = 1
            checkSec.add((row, col))
            moves = [[1,0], [0,1], [-1,0], [0,-1]]
            for move in moves:
                area += islandArea(row+move[0], col+move[1])

            return area

        for row in range(ROWS):
            for col in range(COLS):
                if((row, col) not in checkSec):
                    if(grid[row][col] == 1):
                        maxArea = max(islandArea(row, col), maxArea)
        
        return maxArea
