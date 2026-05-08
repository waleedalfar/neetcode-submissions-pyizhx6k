class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr = []

        ptr1 = 0
        ptr2 = len(numbers) - 1

        for i, n in enumerate(numbers):
            if numbers[ptr1] + numbers[ptr2] == target:
                return [ptr1 + 1, ptr2 + 1]
            
            if numbers[ptr1] + numbers[ptr2] > target:
                ptr2 -= 1

            if numbers[ptr1] + numbers[ptr2] < target:
                ptr1 += 1
            