class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, r = 0, 0
        maxSub = 0

        while r < len(s):
            while s[r] in charSet:
               charSet.remove(s[l])
               l += 1
            charSet.add(s[r])
            maxSub = max(r - l + 1, maxSub)
            r += 1        

        return maxSub
