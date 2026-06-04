class Solution:
    def findMin(self, nums: List[int]) -> int:
        #The numbers simply cannot climb up, drop down, and somehow still end up higher than where they started
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            
        return nums[l]