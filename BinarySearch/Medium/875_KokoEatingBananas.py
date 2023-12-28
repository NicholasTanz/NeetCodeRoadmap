class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPiles = max(piles)
        minVal = maxPiles
        l, r = 1, maxPiles

        # apply binary search and see if mth value holds. 
        while l <= r:
            m = (r + l) // 2 

            # checking if possible to eat during timeframe
            elapsedH = 0
            for pile in piles:
                elapsedH += math.ceil(pile / m)
            
            # not possible - move to right
            if(elapsedH > h):
                l = m + 1
            # possible - try smaller time 
            else:
                r = m - 1
                minVal = min(minVal, m)

        return minVal

