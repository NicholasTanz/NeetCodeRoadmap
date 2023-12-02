class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                tp, i = stack.pop()
                res[i] = (idx - i)
            stack.append((temp, idx))
        
        return res
