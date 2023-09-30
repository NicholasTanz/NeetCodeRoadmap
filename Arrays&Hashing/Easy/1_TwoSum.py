class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store_nums = {}
        for idx,num in enumerate(nums):
            if target-num in store_nums:
                return [store_nums[target-num], idx]
            else:
                store_nums[num] = idx
