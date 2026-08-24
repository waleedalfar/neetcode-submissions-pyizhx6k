class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        pairsS = {}
        pairsT = {}

        for i in range(len(s)):
            pairsS[s[i]] = 1 + pairsS.get(s[i], 0)
            pairsT[t[i]] = 1 + pairsT.get(t[i], 0)

        for item in pairsS:
            if pairsS[item] != pairsT.get(item, 0):
                return False
        return True

        

