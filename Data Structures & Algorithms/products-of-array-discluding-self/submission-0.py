class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for j, nt in enumerate(nums):
            for i, n in enumerate(nums):
                if j != i: 
                    output[j] *= n

        return output


        # go over nums skipping the ith element
        # have a variable that *= all of them and at the end of that loop
        # have a master for loop so that we basically go over the nums array twice