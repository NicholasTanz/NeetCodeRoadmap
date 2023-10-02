class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        present_chars = {}
        l_idx, r_idx = 0, 0
        max_substr = 0
        curr_len = 0
        l_s = len(s)
        if(not l_s):
            return 0
        while r_idx != l_s and l_s - l_idx > max_substr:
            if(s[r_idx] in present_chars):
                if(curr_len > max_substr):
                    max_substr = curr_len
                present_chars = {}
                curr_len=0
                l_idx+=1
                r_idx=l_idx
            else:
                present_chars[s[r_idx]] = True
                curr_len+=1
                r_idx+=1
        if(curr_len > max_substr):
            return curr_len
        return max_substr
# Optimized Solution:
'''
charSet = set()
l, res = 0, 0
for r in range(len(s)):
    while s[r] in charSet:
        charSet.remove(s[l])
        l += 1
    charSet.add(s[r]
    res = max(res, r - 1 + 1)
return res
'''
