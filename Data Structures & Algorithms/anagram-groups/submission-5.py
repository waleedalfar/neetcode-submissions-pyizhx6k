class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # if access non-existent key automatically creates it and gives it an empty list value
        res = defaultdict(list) 

        for s in strs:
            alphas = [0] * 26 # this will be the key

            for ch in s:
                alphas[ord(ch) - ord("a")] += 1

            res[tuple(alphas)].append(s)

        return list(res.values())
        