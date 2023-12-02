class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxS = nums[0]
        l, r = 0, 0
        cur_sub = 0
        while r < len(nums):
            if(cur_sub < 0):
                cur_sub = 0
                l = r

            cur_sub += nums[r]
            maxS = max(cur_sub, maxS)
            r += 1
        
        return maxS
