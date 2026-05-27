class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countK = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            countK[n] = 1 + countK.get(n, 0)
        
        for num, cnt in countK.items():
            freq[cnt].append(num)

        res = []

        for i in range (len(freq) - 1, 0, -1):
            for nums in freq[i]:
                res.append(nums)
                if len(res) == k:
                    return res


