class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {} # val : index

        for i, n in enumerate(nums):
            ind2 = target - n

            if ind2 in dictt:
                return [dictt[ind2], i]

            dictt[n] = i

