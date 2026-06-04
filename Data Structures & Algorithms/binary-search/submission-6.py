class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target > nums[mid]:
                l += 1
            if target < nums[mid]:
                r -= 1
            if target == nums[mid]:
                return mid

        return -1