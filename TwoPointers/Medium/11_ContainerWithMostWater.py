class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_idx, r_idx = 0, len(height)-1
        max_water = 0
        curr_water = 0
        while l_idx <= r_idx:
            min_height = min(height[l_idx], height[r_idx])
            curr_water=min_height*(r_idx-l_idx)
            max_water = max(max_water, curr_water)
            if(height[l_idx] >= height[r_idx]):
                r_idx-=1
            else:
                l_idx+=1
    
        return max_water
