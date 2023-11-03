class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Base case 1: if you try to access an element that is beyond the list - out of bounds
        Base case 2: given each element is strictly positive - if sum becomes larger than target - impossible to reach target
        Base case 3: target == sum (append & return)
        '''

        res = []
        len_l = len(candidates)
        def dfs(i, cur_sum, cur_sub):
            if(cur_sum == target):
                res.append(cur_sub.copy())
                return
            if(i >= len_l or cur_sum >= target):
                return
            
            # chose to include an element - could possibily include it again
            cur_sub.append(candidates[i])
            dfs(i, cur_sum+candidates[i], cur_sub)

            # chose to move to next element and not include cur element
            cur_sub.pop()
            dfs(i+1, cur_sum, cur_sub)

        dfs(0, 0, [])
        return res
