class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        # loop through each string, create an array of length 26
        for s in strs:
            count = [0] * 26

            # for each char in the string do some math that basically gets:
            # count[ord("b") - ord("a")] += 1
            # this means count[1] += 1
            # this represents the frequency for each char in each string in count
            for c in s:
                count[ord(c) - ord("a")] += 1

            # because lists are mutable, they cannot be used as dict keys, so 
            # convert count list to tuple and use as the key for str
            # so the frequency tuple for s = "abc" would be like [1, 1, 1, 0, ... , 0] 
            res[tuple(count)].append(s)

        # return only the values in res, (s in strs)
        # some of the res had multiple s appended to one key,
        # so it returns the values in that way where it prints the
        # [["gdc","cdg"], "abc"] for one key then for the other in 
        return list(res.values())