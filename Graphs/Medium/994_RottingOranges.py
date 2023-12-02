class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue_rotten = []
        fresh_oranges = 0
        # finding all rotten oranges row col && fresh orange count
        for row in range(ROWS):
            for col in range(COLS):
                if(grid[row][col] == 1):
                    fresh_oranges+=1
                elif(grid[row][col] == 2):
                    queue_rotten.append((row, col))
        
        # going through rotten oranges and finding all neighboring possible fresh orange to turn rotten. 
        moves = [[1,0], [0,1], [-1,0], [0,-1]]
        time = 0
        while queue_rotten and fresh_oranges > 0:
            for i in range(len(queue_rotten)): 

                # check all 4 adjacent spots to turn fresh into rotten orange
                row, col = queue_rotten.pop(0)
                for move in moves:
                    checkRow = row+move[0]
                    checkCol = col+move[1]

                    if(checkRow < 0 or checkCol < 0 or checkRow >= ROWS or checkCol >= COLS or grid[checkRow][checkCol] == 0 or grid[checkRow][checkCol] == 2):
                        continue

                    # cell must be a fresh orange - make rotten and add to queue        
                    grid[checkRow][checkCol] = 2
                    fresh_oranges -= 1
                    queue_rotten.append((checkRow, checkCol))
                
            time += 1

        return time if fresh_oranges == 0 else -1
