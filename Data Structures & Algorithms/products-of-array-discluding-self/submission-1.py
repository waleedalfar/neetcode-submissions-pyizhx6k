class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        
        # we start at i = 1 
        # account for that using i - 1 thoughout
        # multiply the last saved prefix value by the current nums value in the arr (i = 1; i - 1 this will result in i = 0
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1] 
        
        # starts at index = 2 or the 3rd element, uses suffix[3] * nums[3], 1 * 6 = 6
        for j in range(len(nums) - 2, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j + 1]

        output = [1] * len(nums)

        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i]

        return output


        
        