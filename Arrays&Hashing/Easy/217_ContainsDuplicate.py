class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
            hash = {}

            for i, n in enumerate(nums):
                if(nums[i] in hash):
                    return True
                hash[n] = 0
            return False
