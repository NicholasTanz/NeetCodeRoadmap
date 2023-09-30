class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = defaultdict(int)
        if len(s) != len(t):
            return False
             
        for c in s:
            hash[c] +=1
        
        for c in t:
            if c in hash:
                hash[c] -= 1
                if hash[c] == 0:
                    del hash[c]


        if len(hash) == 0:
            return True
        return False
