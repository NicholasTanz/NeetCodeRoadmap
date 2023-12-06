class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_ = nums[0]
        while l <= r:
            if(nums[l] <= nums[r]):
                min_ = min(min_, nums[l])
                break
            
            m = (l + r) // 2
            min_ = min(nums[m], min_)
            if(nums[m] >= nums[l]):
                l = m + 1
            else:
                r = m - 1
        
        return min_
