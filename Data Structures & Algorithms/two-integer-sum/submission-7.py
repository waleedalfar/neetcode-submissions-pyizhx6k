class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in pairs:
                return [pairs[difference], i]
            
            pairs[n] = i 