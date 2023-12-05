class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2 
            if(nums[m] == target):
                return m

            if(nums[l] <= nums[m]): # means sorted left portion 
                if(target < nums[l] or target > nums[m]): # should traverse right side; as target cannot be in left side. 
                    l = m + 1
                else:
                    r = m - 1
            else: # this means right side must be sorted. 
                if(target < nums[m] or target > nums[r]): # should traverse left side; as target cannot be in right side
                    r = m - 1 
                else:
                    l = m + 1 
        
        return -1 
