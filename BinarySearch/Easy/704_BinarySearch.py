class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_idx = 0
        r_idx = len(nums)-1
        mid_idx = r_idx // 2
        while(l_idx < r_idx and nums[l_idx] != target and nums[r_idx] != target and nums[mid_idx] != target):
            #means on left side - if it exists
            if(nums[mid_idx] > target):
                l_idx+=1
                r_idx=mid_idx-1
                mid_idx = r_idx // 2
            #means on right side - if it exists
            else:
                l_idx=mid_idx+1
                r_idx-=1
                mid_idx = (l_idx+r_idx) // 2
        if(nums[l_idx] == target):
            return l_idx
        elif(nums[r_idx] == target):
            return r_idx
        else:
            return mid_idx if nums[mid_idx]==target else -1
            
        

            
