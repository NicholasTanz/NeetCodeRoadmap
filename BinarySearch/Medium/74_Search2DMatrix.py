class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #simply returning false if target exceed greatest value or least value; or true if target is greatest/least value. 
        if matrix[-1][-1] < target or matrix[0][0] > target:
            return False
        if matrix[-1][-1] == target or matrix[0][0] == target:
            return True

        # utilizing lower & upper limits to determine if target within matrix
        lower_lim_idx = 0
        upper_lim_idx = 0
        if len(matrix) >=  2:
            #finding the upper limit
            while matrix[upper_lim_idx][-1] < target:
                upper_lim_idx +=1

            #finding the lower limit
            while matrix[lower_lim_idx + 1][0] <= target:
                    lower_lim_idx +=1
                    if(matrix[lower_lim_idx][0] == target or matrix[lower_lim_idx] == matrix[-1]):
                        break

            # returning false if the limits aren't the same --> they should be same - indicates target may fall within some list
            if lower_lim_idx != upper_lim_idx:
                return False

        # simple binary search at lower lim list; or higher, should be same. 
        search_list = matrix[lower_lim_idx]
        low_idx = 0
        high_idx = len(search_list) - 1
        mid_idx = high_idx // 2

        while search_list[low_idx] != target and search_list[mid_idx] != target and search_list[high_idx] != target:
            if search_list[mid_idx] < target:
                high_idx -= 1
                low_idx = mid_idx + 1
                mid_idx = (high_idx + low_idx) // 2
                
            if search_list[mid_idx] > target:
                high_idx = mid_idx - 1
                low_idx += 1
                mid_idx = (high_idx) // 2

            if high_idx < low_idx:
                return False
        
        return True
