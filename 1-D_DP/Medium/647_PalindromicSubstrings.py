class Solution:
    def countSubstrings(self, s: str) -> int:
        numPalis = 0
        for i in range(len(s)):
            # odd palis
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                numPalis += 1
                r += 1
                l -= 1  
            # even palis
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                numPalis += 1
                r += 1
                l -= 1

        return numPalis 
