class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()

        for n in nums:
            hset.add(n)

        if len(nums) != len(hset):
            return True
        return False
