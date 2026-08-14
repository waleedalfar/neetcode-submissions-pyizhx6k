class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sset = set()

        for n in nums:
            if n in sset:
                return True
            else:
                sset.add(n)

        return False