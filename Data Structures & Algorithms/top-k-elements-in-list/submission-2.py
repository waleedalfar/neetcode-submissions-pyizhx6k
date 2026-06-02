class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        pairs = {} # element -> count
        freq = [[] for i in range(len(nums) +1)] # [count] = [[elements]]

        for n in nums:
            pairs[n] = 1 + pairs.get(n, 0)

        for n, c in pairs.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res