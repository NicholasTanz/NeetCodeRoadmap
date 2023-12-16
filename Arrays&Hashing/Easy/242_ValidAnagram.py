class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLets = [0] * 26
        for char in s:
            sLets[ord(char) - ord('a')] += 1
        
        tLets = [0] * 26
        for char in t:
            tLets[ord(char) - ord('a')] += 1
        
        return tuple(tLets) == tuple(sLets)
