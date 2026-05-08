class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pairs = {}

        for i, n in enumerate(numbers):
            diff = target - n

            if diff in pairs:
                return [pairs[diff] + 1, i + 1] 
            
            pairs[n] = i
            