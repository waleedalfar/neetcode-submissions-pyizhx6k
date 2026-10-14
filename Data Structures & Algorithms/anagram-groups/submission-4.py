class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        # key: list of the frequency of each letter in a word
        # value: word that corresponds with the keys list

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s) # convert to tuple cuz its  immutable which makes it hashable which makes it eligible to be a key in a hashmap

        return list(res.values())
