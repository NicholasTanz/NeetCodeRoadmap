class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for idx, val in enumerate(nums):
            if(nums[abs(val)-1] < 0):
                return abs(val)
            else:
                # utilizing fact that all nums in nums are [1, n] (positive); multiplying by -1 allows me to tell if num at idx of val has alrdy been *=-1, thus duplicated num. 
                nums[abs(val)-1]*=-1 
