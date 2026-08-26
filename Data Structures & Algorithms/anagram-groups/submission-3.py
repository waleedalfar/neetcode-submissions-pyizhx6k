class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 
        # key: number of letters in each word
        # value: words that correspond with the num of chars

        # generate list alphabetic frequencies for each string
        for s in strs:
            count = [0] * 26 # list of 26 elements all with the val of 0

            # for each char in each string count em up
            for c in s:
                count[ord(c) - ord("a")] += 1

            # append each word with the same count key
            res[tuple(count)].append(s)

        return list(res.values())