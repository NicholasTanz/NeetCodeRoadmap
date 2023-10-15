class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_vals = {}
        col_vals = {}
        threeXthree_vals = {}
        # check to make sure no col / row has repeated val
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if(board[row][col] == "."):
                    continue
                
              # checking if the current val is already in a given row
                if(row in row_vals):
                    if(board[row][col] in row_vals[row]):
                        return False
                    else:
                        row_vals[row].add(board[row][col])
                else:
                    row_vals[row] = set(board[row][col])

                # checking if the current val is already in a given col
                if(col in col_vals):
                    if(board[row][col] in col_vals[col]):
                        return False
                    else:
                        col_vals[col].add(board[row][col])
                else:
                    col_vals[col] = set(board[row][col])
                  
                # checking if the current val is already in 3x3 group
                if (row // 3, col // 3) in threeXthree_vals:
                    if(board[row][col] in threeXthree_vals[(row//3,col//3)]):
                        return False
                    else:
                        threeXthree_vals[(row//3, col//3)].add(board[row][col])
                else:
                    threeXthree_vals[(row//3,col//3)] = set(board[row][col])
        return True
