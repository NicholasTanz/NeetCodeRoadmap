class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])
        target_row = -1
        for i in range(0, ROWS):
            if(target >= matrix[i][0] and target <= matrix[i][COLS - 1]):
                target_row = i
                break
        
        # in-between two rows - straddles and thus cannot be contained. 
        if(target_row == -1):
            return False

        # perform a binary search at that row. 
        l_idx = 0
        h_idx = COLS - 1
        m_idx = h_idx // 2 

        while l_idx < h_idx and matrix[target_row][l_idx] != target and matrix[target_row][m_idx] != target and matrix[target_row][h_idx] != target:
            if(matrix[target_row][m_idx] < target):
                l_idx = m_idx + 1
                h_idx -= 1
                m_idx = (l_idx + h_idx) // 2
            else:
                l_idx += 1
                h_idx = m_idx - 1
                m_idx = (l_idx + h_idx) // 2
        
        if(matrix[target_row][l_idx] == target or matrix[target_row][m_idx] == target or matrix[target_row][h_idx] == target):
            return True
        
        return False



