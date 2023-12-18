class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heap ds - multiply by -1 to implement max heap 
        stones = [stone * -1 for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            largest2 = heapq.heappop(stones)
            if largest != largest2:
                heapq.heappush(stones, largest - largest2)
        
        return 0 if len(stones) == 0 else abs(stones[0])
