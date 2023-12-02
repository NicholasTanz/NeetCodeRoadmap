class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        
        def helpRob(ary):
            rob1, rob2 = 0, 0
            for num in ary:
                temp = max(rob1+num, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(helpRob(nums[:len(nums)-1]), helpRob(nums[1:]))
