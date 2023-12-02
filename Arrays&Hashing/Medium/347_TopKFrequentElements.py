class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # stores the values and number of times that value occurs
        val_counts = {}
        for num in nums:
            if num in val_counts:
                val_counts[num] += 1
            else:
                val_counts[num] = 1

       
        heap = []
        for val, count in val_counts.items():
            heapq.heappush(heap, (count, val))
            if(len(heap) > k):
                heapq.heappop(heap)
        
        return [pair[1] for pair in heap]
