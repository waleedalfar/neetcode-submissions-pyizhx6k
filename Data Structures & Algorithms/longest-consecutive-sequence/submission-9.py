class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()

        streak = 1
        max_streak = 1

        for i, n in enumerate(nums):
            if i > 0:

                if n == nums[i - 1]:
                    continue

                if n == nums[i - 1] + 1: # if previous is less than current this is a consecutive
                    streak += 1
                    if streak > max_streak:
                        max_streak = streak
                else:
                    streak = 1
            else:
                streak = 1
        
        return max_streak
                    

