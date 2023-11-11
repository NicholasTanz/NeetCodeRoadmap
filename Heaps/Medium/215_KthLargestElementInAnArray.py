class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_ = nums[:k]
        heapq.heapify(heap_)

        for val in nums[k:]:
            heapq.heappushpop(heap_, val)
        
        return heap_[0]
