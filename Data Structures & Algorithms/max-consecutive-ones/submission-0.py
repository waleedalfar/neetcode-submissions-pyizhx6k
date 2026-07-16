class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxcount = 0

        for n in nums:
            count = count + 1 if n else 0
            maxcount= max(maxcount, count)
        return maxcount