class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heap.append([point[0]**2 + point[1]**2, point[0], point[1]])
        
        heapq.heapify(heap)

        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1:])
            k-=1
        
        return res
