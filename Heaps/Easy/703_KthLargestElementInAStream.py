class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = nums[:k]
        heapq.heapify(self.pq)

        for val in nums[k:]:
            heapq.heappushpop(self.pq, val)

    def add(self, val: int) -> int:
        if(len(self.pq) < self.k):
            heapq.heappush(self.pq, val)
        else:
            heapq.heappushpop(self.pq, val)
        
        return self.pq[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
