class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        sub_set = []
        def dfs(i):
            if i == len(nums):
                res.append(sub_set[::])
            if i >= len(nums):
                return
            
            # chose to include value
            sub_set.append(nums[i])
            dfs(i+1)

            # chose not to include value
            sub_set.pop()
            dfs(i+1)
        
        dfs(0)
        return res
