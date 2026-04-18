class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        k = 0 # longest

        for n in numSet:
            # check if start of sequence# e.g 99 does not exisit when n = 100, then 100 is the start
            if (n - 1) not in numSet: 
                length = 0
                # check 100, 101, 102, ...
                while (n + length) in numSet:
                    length += 1
                k = max(length, k) # if length is the new biggest potential k then update
        return k

