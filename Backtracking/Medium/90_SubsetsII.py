class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        len_nums = len(nums)

        def dfs(i, cur_sub):
            if i == len_nums:
                res.append(cur_sub[::])
            if i >= len_nums:
                return
            

            # chose to include a val for the set
            cur_sub.append(nums[i])
            dfs(i+1, cur_sub)

            # chose not to include a val for the set - should NOT include any occurences for that value
            cur_sub.pop()
            while i + 1 < len_nums and nums[i] == nums[i + 1]:
                i+=1
            dfs(i+1, cur_sub)
        
        dfs(0, [])
        return res
