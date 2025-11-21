class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        for c in set(s):  
            l = s.find(c)
            r = s.rfind(c)
            if l < r:
                mid_chars = set(s[l+1:r])
                for m in mid_chars:
                    res.add((c, m))
        return len(res)