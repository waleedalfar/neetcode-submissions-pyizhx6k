class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        res = 0

        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet: # once a duplicate has been found,
                                    # zxyzx,
                                    # found zxy
                                    # found ...z must remove left z
                                    # found xyz theres still an x
                                    # found ...x must remove left x
                                    # yxz
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
            

